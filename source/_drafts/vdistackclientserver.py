# -*- coding:utf8 -*-
from twisted.internet import protocol, reactor, endpoints
from twisted.protocols import basic
import os
import json
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vdistackclientadmin.settings")

from portal.models import VDIClient
import gettext
gettext.bindtextdomain("vdistackclientadmin", "locale/")
gettext.textdomain("vdistackclientadmin")
_ = gettext.gettext
import datetime

RESULT_CODE = {
    "0": _(u"ok"),

    # 1 其他错误
    "1000": _(u"json format error"),
    "1001": _(u"result key error"),
    "1002": _(u"method not define error"),
    "1003": _(u"method func failed error"),

    # 4 登录请求错误
    "4000": _(u"client_uuid or mac_address can not be null"),
    "4001": _(u"client_uuid or mac_address not found or not match"),
}

# method: ***
# method_type: Request, Response
# if method_type is Response
# code
# code_message
# message


class ResposeMethod(object):
    def __init__(self, method, **kwargs):
        if isinstance(method, RequestMethod):
            method = method.method
        self.method_type = kwargs.get("method_type", "response")
        self.method = method
        self.kwargs = kwargs

    def get_response_message(self, **kwargs):
        msg = {"method": self.method,
               "method_type": self.method_type}
        msg.update(self.kwargs)
        msg.update(kwargs)

    def error_message(self, code, message=None, **kwargs):
        """
        对该请求返回的错误信息
        :param message:
        :param kwargs:
        :return:
        """
        code_message = RESULT_CODE.get(str(code), _(u"undefine code"))
        msg = {"code_message": code_message,
               "code": code,
               "method": self.method,
               "method_type": "response"}
        if message:
            msg["message"] = message
        return json.dumps(msg)

    @staticmethod
    def result_message(code, message=None, **kwargs):
        code_message = RESULT_CODE.get(str(code), _(u"undefine code"))
        msg = {"code_message": code_message,
               "code": code,
               "method": "error",
               "method_type": "response"}
        if message:
            msg["message"] = message
        return json.dumps(msg)


class RequestMethod(object):
    def __init__(self, method, **kwargs):
        self.method_type = kwargs.get("method_type", "request")
        self.method = method
        self.kwargs = kwargs

    def get_request_message(self, **kwargs):
        msg = {"method": self.method,
               "method_type": self.method_type}
        msg.update(self.kwargs)
        msg.update(kwargs)
        return json.dumps(msg)


class VDIStackClientServerProtocol(basic.LineReceiver):
    def __init__(self, factory):

        self.factory = factory

        # 是否登陆默认为未登陆
        self.is_login = False

        # 记录客户端连接的时间，一定时间连接后踢掉该客户端
        self.connected_time = None

    def lineReceived(self, data):
        """数据接收回调函数，注意要注意缓存接收数据"""
        # try:
        self.dealJsonMessage(json.loads(data))
        # except Exception, e:
        #     self.sendLine(ResposeMethod.result_message(1000, e.message))

    def connectionMade(self):
        """ 当连接创建回调函数"""

        self.connected_time = datetime.datetime.now()

        self.factory.clients.append(self)

        # 发送请求让客户端发送登陆请求
        self.sendLine(RequestMethod("login").get_request_message(message=_(u"please input mac_address and client_uuid")))

    def connectionLost(self, reason):
        """连接断开回调函数"""
        self.factory.clients.remove(self)

    # noinspection PyPep8Naming
    def dealJsonMessage(self, data):
        method = data.get("method", "undefine")
        method_func = getattr(self, "cmd_"+method, None)
        if method_func:
            method_func(method, data)
        else:
            self.sendLine(ResposeMethod.result_message(1002))
        return

    def cmd_login(self, method, data):
        """
        处理登录数据
        :param data: 登录请求的数据
        :return:
        """
        client_uuid = data.get("client_uuid", None)
        mac_address = data.get("mac_address", None)
        response = ResposeMethod(method)
        if not client_uuid or not mac_address:
            return response.error_message(4000)
        if not VDIClient.objects.filter(client_uuid=client_uuid, mac_address=mac_address).exists():
            return response.error_message(4001)
        self.is_login = True
        self.sendLine(response.error_message(0))

    def cmd_undefine(self, method, data):
        self.sendLine(ResposeMethod.result_message(1002))

class VDIStackClientServerProtocolFactory(protocol.Factory):

    def __init__(self):
        # factory中的所有客户端
        self.clients = []

    def buildProtocol(self, addr):
        return VDIStackClientServerProtocol(self)


class VDIStackClientAdminServerProtocol(basic.LineReceiver):
    """
    用于管理端的连线
    """
    def __init__(self, admin_factory, client_factory):

        self.admin_factory = admin_factory
        self.client_factory = client_factory

    def connectionMade(self):
        """ 当连接创建回调函数"""
        self.admin_factory.clients.append(self)

        # 发送请求让客户端发送登陆请求
        self.sendLine(RequestMethod("method").get_request_message(message=_(u"please send request method")))

    def connectionLost(self, reason):
        """连接断开回调函数"""
        self.admin_factory.clients.remove(self)

    def lineReceived(self, data):
        """数据接收回调函数，注意要注意缓存接收数据"""
        # try:
        self.dealJsonMessage(json.loads(data))
        # except Exception, e:
        #     self.sendLine(ResposeMethod.result_message(1000, e.message))

    def dealJsonMessage(self, data):
        method = data.get("method", "undefine")
        method_func = getattr(self, "cmd_"+method, None)
        if method_func:
            method_func(method, data)
        else:
            self.sendLine(ResposeMethod.result_message(1002))
        return

    def cmd_getOnlineClients(self, method, data):
        print self.client_factory.clients
        return self.sendLine(ResposeMethod(method).error_message(0))


class VDIStackClientAdminProtocolFactory(protocol.Factory):

    def __init__(self, client_server):
        # factory中的所有客户端
        self.clients = []
        self.client_factory = client_server

    def buildProtocol(self, addr):
        return VDIStackClientAdminServerProtocol(self, self.client_factory)



def main():
    client_server = VDIStackClientServerProtocolFactory()
    admin_server = VDIStackClientAdminProtocolFactory(client_server)
    reactor.listenTCP(1234, client_server)
    reactor.listenTCP(1235, admin_server)
    reactor.run()

if __name__ == "__main__":
    main()
