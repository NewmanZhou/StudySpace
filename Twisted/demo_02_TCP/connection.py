# -*- coding: utf-8 -*-
# @Time   : 2019/12/29 3:51 下午
# @Author : NewmanZhou
# @Desc : ==============================================
# Life is Short I Use Python!!!                      ===
# If this runs wrong,don't ask me,I don't know why;  ===
# If this runs right,thank god,and I don't know why. ===
# Maybe the answer,my friend,is blowing in the wind. ===
# ======================================================
# @Project : StudySpace
# @FileName: connection.py
# @Software: PyCharm

from twisted.internet.protocol import Protocol, ClientFactory


class Echo(Protocol):  # Protocol 子类，此处进行通信逻辑开发
    def __init__(self):
        self.connected = False

    def connectionMade(self):
        self.connected = True

    def connectionLost(self, reason):
        self.connected = False

    def dataReceived(self, data):
        print(data.decode("utf8"))


class EchoClientFactory(ClientFactory):  # Factory 子类，管理连接关系
    def __init__(self):
        self.protocol = None

    def startedConnecting(self, connector):
        print("start to connect")

    def buildProtocol(self, addr):
        print("Connected")
        self.protocol = Echo()
        return self.protocol

    def clientConnectionLost(self, connector, reason):
        print("Lost Connection. Reason:", reason)

    def clientConnectionFailed(self, connector, reason):
        print("Connection Failed. Reason:", reason)


from twisted.internet import reactor
import threading
import fileinput
import time
import sys
import datetime

bStop = False


def routine(factory):  # 每隔5秒向服务器发送消息
    while not bStop:
        if factory.protocol and factory.protocol.connected:
            factory.protocol.transport.write("hello, I'm %s  %s ".encode("utf8"))
        time.sleep(3)
host = "127.0.0.1"
port = 8007
factory = EchoClientFactory()
reactor.connectTCP(host, port, factory)
threading.Thread(target=routine, args=(factory,)).start()
reactor.run()
bStop = True
