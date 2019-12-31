# -*- coding: utf-8 -*-
# @Time   : 2019/12/29 2:58 下午
# @Author : NewmanZhou
# @Desc : ==============================================
# Life is Short I Use Python!!!                      ===
# If this runs wrong,don't ask me,I don't know why;  ===
# If this runs right,thank god,and I don't know why. ===
# Maybe the answer,my friend,is blowing in the wind. ===
# ======================================================
# @Project : StudySpace
# @FileName: Spreader.py
# @Software: PyCharm
from twisted.internet.protocol import Protocol

clients = []


class Spreader(Protocol):
    def __init__(self, factory):
        self.factory = factory

    def connectionMade(self):
        self.factory.numProtocols = self.factory.numProtocols + 1
        self.transport.write(
            (u"欢迎来到Spread Site, 您是第%d个客户端用户！\n " %
             (self.factory.numProtocols)).encode("utf8")
        )
        print("new contect: %d" % self.factory.numProtocols)
        clients.append(self)

    def connectionLost(self, reason):
        self.factory.numProtocols = self.factory.numProtocols - 1
        clients.remove(self)
        print("lost contect: %d" % self.factory.numProtocols)

    def dataReceived(self, data):
        if data == "close":
            self.transport.loseConnection()
            for client in clients:
                if client != self:
                    client.transport.write(data)


from twisted.internet.protocol import Factory
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor


class SpreadFactory(Factory):
    def __init__(self):
        self.numProtocols = 0

    def buildProtocol(self, addr):
        return Spreader(self)


endpoint = TCP4ServerEndpoint(reactor, 8007)
endpoint.listen(SpreadFactory())
reactor.run()
