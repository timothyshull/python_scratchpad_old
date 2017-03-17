import re

test_str = """
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: eno16777984: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP qlen 1000
    link/ether 00:50:56:a2:cd:71 brd ff:ff:ff:ff:ff:ff
    inet 172.22.29.65/24 brd 172.22.29.255 scope global dynamic eno16777984
       valid_lft 428621sec preferred_lft 428621sec
    inet6 fe80::250:56ff:fea2:cd71/64 scope link
       valid_lft forever preferred_lft forever
2: eno16777985: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP qlen 1000
    link/ether 00:50:56:a2:cd:72 brd ff:ff:ff:ff:ff:ff
    inet 172.22.29.66/24 brd 172.22.29.255 scope global dynamic eno16777984
       valid_lft 428621sec preferred_lft 428621sec
    inet6 fe80::250:56ff:fea2:cd71/64 scope link
       valid_lft forever preferred_lft forever
"""

mac_addr = "00:50:56:a2:cd:71"
# re_str = re.escape('{0}.*inet\s([\d.]*)\s'.format(mac_addr))
re_str = '{0}.*inet\s([\d./]*)\s'.format(mac_addr)

mo = re.search(re_str, test_str, re.DOTALL | re.MULTILINE)

if mo:
    network = '.'.join(mo.group(1).split('.')[:3] + [str(0)])
    print(network)
