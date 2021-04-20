# -*- coding: utf-8 -*-
# @Time   : 2021/1/20 8:47 下午
# @Author : NewmanZhou
# @Desc : ==============================================
# Life is Short I Use Python!!!                      ===
# If this runs wrong,don't ask me,I don't know why;  ===
# If this runs right,thank god,and I don't know why. ===
# Maybe the answer,my friend,is blowing in the wind. ===
# ======================================================
# @Project : StudySpace
# @FileName: ipaddress_addresses.py
# @Software: PyCharm
'''
IP就是TCP/IP协议族中网络层的一种互联协议。
IPv4与IPv6后面的数字其实是指的协议版本号，你可以理解为V4.0版本和V6.0版本

1、IPV4与IPV6最多支持多少个物理设备？
IPv4地址长度是32，支持的物理地址是2^32-1个地址；
IPv6地址的长度是128，支持的物理地址是2^128-1个地址。

2、IPV6相比较IPV4有什么优势？
    1、更大的地址空间，IPV6地址容量巨大。
    2、iPV6地址分配遵循Aggregation原则，路由器的路由表长度减少，提高转发数据包的速度。

3、IPv4的回路地址为: 127.0.0.1，
IPv6的回路地址为 : 000:0000:0000:0000:0000:0000:0000:0001 可以简写为 ::1。
'''
#   二进制数据和ASCII之间的转换 binary  ASCII  转换
#   一个快速、轻量级的IPv4/IPv6操作库。这个库用于创建/刺探/操作IPv4和IPv6地址和网络。
# https://pymotw.com/3/ipaddress/index.html
import binascii
import ipaddress


'''
最基本的对象表示网络地址本身。
将字符串、整数或字节序列传递给ip_address()以构造一个地址。
返回值将是IPv4Address或IPv6Address实例，这取决于所使用的地址类型。
'''
def demo_ip_address():
    ADDRESSES = [
        '10.9.0.6',
        'fdfd:87b5:b475:5e3e:b1bc:e121:a8eb:14aa',
    ]

    for ip in ADDRESSES:
        # 入参： 字符串或整数，IP地址。可以提供IPv4或IPv6地址;小于2**32的整数会默认情况下被认为是IPv4。
        addr = ipaddress.ip_address(ip)
        print('{!r}'.format(addr))
        print('   IP version:', addr.version)
        print('   is private:', addr.is_private) #测试此地址是否分配给私有网络。
        # 二进制数据的十六进制表示 ,内层： 该地址的二进制表示形式。
        print('  packed form:', binascii.hexlify(addr.packed))
        print('      integer:', int(addr))
        print()

'''
网络是由一系列地址定义的。它通常用一个基址和一个掩码来表示，
该掩码指示地址的哪些部分代表网络，以及剩余的哪些部分代表网络上的地址。
掩码可以显式地表示，也可以像下面的例子那样使用前缀长度值。
网络是由一系列地址定义的。它通常用一个基址和一个掩码来表示，
该掩码指示地址的哪些部分代表网络，以及剩余的哪些部分代表网络上的地址。
掩码可以显式地表示，也可以像下面的例子那样使用前缀长度值。

和地址一样，IPv4和IPv6网络也有两类网络。每个类都提供属性或方法来访问与网络相关的值，
例如广播地址和网络上可供主机使用的地址。
'''
def demo_ip_network():
    NETWORKS = [
        '10.9.0.0/24',
        'fdfd:87b5:b475:5e3e::/64',
    ]

    for n in NETWORKS:
        # 获取一个IP字符串/int并返回一个正确类型的对象。
        #
        # 参数:
        # 地址:字符串或整数，表示IP网络。IPv4或
        # 可以提供IPv6网络;小于2**32的整数会
        # 默认情况下被认为是IPv4。
        #
        # 返回:
        # IPv4Network或IPv6Network对象。
        net = ipaddress.ip_network(n)
        print('{!r}'.format(net))
        print('     is private:', net.is_private)
        print('      broadcast:', net.broadcast_address)  # address objects
        print('     compressed:', net.compressed) # 以字符串形式返回IP地址的简写版本。
        print('   with netmask:', net.with_netmask) # 子网掩码
        print('  with hostmask:', net.with_hostmask) # 主机掩码
        print('  num addresses:', net.num_addresses) # 当前子网内主机的个数
        print()

# 网络实例是可迭代的，并产生网络上的地址。
def demo_for_ip_network():
    NETWORKS = [
        '10.9.0.0/24',
        'fdfd:87b5:b475:5e3e::/64',
    ]

    for n in NETWORKS:
        net = ipaddress.ip_network(n)
        print('{!r}'.format(net))
        for i, ip in zip(range(5), net):
            print(ip)
        print()
'''
在网络上迭代会产生地址，但并非所有地址都对主机有效。
例如，网络的基址和广播地址都包括在内。
要找到网络上常规主机可以使用的地址，请使用hosts()方法，它会生成一个生成器。
'''
def demo_ip_network_host():
    NETWORKS = [
        '10.9.0.0/24',
        'fdfd:87b5:b475:5e3e::/64',
    ]

    for n in NETWORKS:
        net = ipaddress.ip_network(n)
        print('{!r}'.format(net))
        print(list(zip(range(3), net.hosts())))
        # net.hosts  在网络中可用的主机上生成迭代器。
        for i, ip in zip(range(3), net.hosts()):
            print(ip)
            print(type(ip))
        print()

'''
除了迭代器协议之外，网络还支持 in 操作符来确定一个地址是否是网络的一部分。
in 的实现使用网络掩码来测试地址，因此它比在网络上展开完整的地址列表更有效。
'''
def demo_is_ip_in_network():
    NETWORKS = [
        ipaddress.ip_network('10.9.0.0/24'),
        ipaddress.ip_network('fdfd:87b5:b475:5e3e::/64'),
    ]

    ADDRESSES = [
        ipaddress.ip_address('10.9.0.6'),
        ipaddress.ip_address('10.7.0.31'),
        ipaddress.ip_address(
            'fdfd:87b5:b475:5e3e:b1bc:e121:a8eb:14aa'
        ),
        ipaddress.ip_address('fe80::3840:c439:b25e:63b0'),
    ]

    for ip in ADDRESSES:
        for net in NETWORKS:
            if ip in net:
                print('{}\nis on {}'.format(ip, net))
                break
        else:
            print('{}\nis not on a known network'.format(ip))
        print()

'''
网络接口表示网络上的特定地址，可以用主机地址和网络前缀或网络掩码表示。

ip_interface(ip):
获取一个IP字符串/int并返回一个正确类型的对象。
参数:
address:字符串或整数，IP地址。IPv4或
可以提供IPv6地址;小于2**32的整数会
默认情况下被认为是IPv4。
返回:
IPv4Interface或IPv6Interface对象

接口对象具有可以分别访问整个网络和寻址的属性，以及表示接口和网络掩码的几种不同方式。
'''
def demo_ip_interface():
    ADDRESSES = [
        '10.9.0.6/24',
        'fdfd:87b5:b475:5e3e:b1bc:e121:a8eb:14aa/64',
    ]

    for ip in ADDRESSES:
        iface = ipaddress.ip_interface(ip)
        print('{!r}'.format(iface))
        print('network:\n  ', iface.network)
        print('ip:\n  ', iface.ip)
        print('IP with prefixlen:\n  ', iface.with_prefixlen)
        print('netmask:\n  ', iface.with_netmask)
        print('hostmask:\n  ', iface.with_hostmask)
        print()

if __name__ == '__main__':
    # demo_ip_address()
    # demo_ip_network()
    # demo_for_ip_network()
    # demo_ip_network_host()
    # demo_is_ip_in_network()
    demo_ip_interface()