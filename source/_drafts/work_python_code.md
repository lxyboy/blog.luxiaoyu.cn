from uuid import getnode as get_mac
mac = get_mac()
':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))


pip install netifaces

import netifaces
netifaces.ifaddresses('eth0')[netifaces.AF_LINK][0]['addr']