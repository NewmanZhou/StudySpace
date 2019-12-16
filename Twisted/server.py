# -*- coding: utf-8 -*-
# @Time   : 2019/12/5 1:41 下午
# @Author : NewmanZhou
# @Desc : ==============================================
# Life is Short I Use Python!!!                      ===
# If this runs wrong,don't ask me,I don't know why;  ===
# If this runs right,thank god,and I don't know why. ===
# Maybe the answer,my friend,is blowing in the wind. ===
# ======================================================
# @Project : StudySpace
# @FileName: service.py
# @Software: PyCharm
from twisted.internet import reactor
from twisted.internet.protocol import Protocol, Factory

'''
Factory：
每个服务器与客户端都会有一个工厂。他负责创建连接。并创建 protocol 对象。

Protocols:
Protocols 描述了如何以异步的方式处理网络中的事件。当连接创建成功后，Factory 会创建一个 protocol, 由 protocol 进行通信。

Transports
Transports 代表网络中两个通信结点之间的连接。Transports负责描述连接的细节，
比如连接是面向流式的还是面向数据报的，流控以及可靠性。

Transports 实现了 ITransports 接口，它包含如下的方法：

-- write方法： 以非阻塞的方式按顺序依次将数据写到物理连接上。
-- writeSequence方法： 将一个字符串列表写到物理连接上。
-- loseConnection 方法：将所有挂起的数据写入，然后关闭连接。
-- getPeer方法： 取得连接中对端的地址信息。
-- getHost方法： 取得连接中本端的地址信息。

Protocols 实现了 IProtocol 接口，它包含如下的方法：
-- makeConnection方法： 在 transport 对象和服务器之间建立一条连接。
-- connectionMade方法： 连接建立起来后调用。
-- dataReceived方法： 接收数据时调用。
-- connectionLost方法： 关闭连接时调用。

Reactor 模式：
Twisted 实现了设计模式中的反应堆（reactor）模式，
这种模式在单线程环境中调度多个事件源产生的事件到它们各自的事件处理例程中去。
Twisted 的核心就是 reactor 事件循环。Reactor 可以感知网络、文件系统以及定时器事件。
它等待然后处理这些事件。
'''

class SimpleProtocol(Protocol):

    # 连接建立起来后调用。
    def connectionMade(self):
        # 客户端连入后向客户端发送一条消息
        print("请求的客户端地址 ")
        print(self.transport.client)
        self.transport.write("消息来自服务端，连接成功".encode('utf-8'))

    # 关闭连接时调用
    def connectionLost(self, reason):
        print(self.transport.client)
        print(reason)

    # 接收数据时调用。
    def dataReceived(self, data):
        print(data.decode('utf-8'))


factory = Factory()
factory.protocol = SimpleProtocol

reactor.listenTCP(9001, factory)
reactor.run()
