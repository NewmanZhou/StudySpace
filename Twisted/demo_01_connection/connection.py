# -*- coding: utf-8 -*-
# @Time   : 2019/12/5 1:49 下午
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
from twisted.internet.protocol import ClientFactory, Protocol
from twisted.internet import reactor


class Sender(Protocol):
    def connectionMade(self):
        """连接成功后调用"""
        self.send_command()

    def send_command(self):
        """连接成功后调用他向服务端发送数据"""
        self.transport.write("我是客户端的请求".encode('utf-8'))

    def dataReceived(self, data):
        """进行数据的接受"""
        print(data.decode('utf-8'))


class BasicClientFactory(ClientFactory):
    def __init__(self, protocol):
        self.protocol = protocol

    def clientConnectionLost(self, connector, reason):
        print('Lost connection:')
        print(reason.getErrorMessage())


PORT = 9001
HOST = '127.0.0.1'

# 实例化工厂对象
test = BasicClientFactory(Sender)
# 连接服务器
reactor.connectTCP(HOST, PORT, test)

reactor.run()
