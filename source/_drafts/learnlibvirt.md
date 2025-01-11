#libvirt 使用

##Connection URIs 连接URI

### 给libvirt指定URIs

URI做为名字传递给*virConnectOpen*或者*virConnectOpenReadOnly*.例子：

```c
virConnectPtr conn = virConnectOpenReadOnly("test:///default");
```

### 配置URI的别名

