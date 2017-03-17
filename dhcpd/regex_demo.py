import re

test_str = """
host testhost.com {
  dynamic;
  hardware ethernet 52:22:00:ae:c3:f4;
  fixed-address 172.22.25.23;
        supersede server.filename = "pxelinux.0";
        supersede server.next-server = c0:a8:6c:de;
        supersede host-name = "testhost.com";
}
"""


def test_one():
    # re.findall('')
    # mo = re.search('^\s{2}dynamic', test_str)
    # mo = re.match('\s*dynamic', test_str)
    # print(mo)
    # if mo:
    #     print(mo.group(0))
    # print(mo.group(1))
    # for item in mo:
    #     print(item)

    # mo = re.findall('.sede', test_str)
    # if mo:
    #     for item in mo:
    #         print(item)
    mo = re.findall('((?:\w{2}:){5}\w{2})', test_str)
    for item in mo:
        print(item)

    mo = re.findall('((?:\d{1,3}\.){3}\d{1,3})', test_str)
    for item in mo:
        print(item)

    # (?!-)[A - Z - _\\d]{1, 63}(? < !-)$'
    mo = re.findall('((?:[A-Za-z0-9\-_]{1,63}\.){2,63}[A-Za-z0-9\-_]{1,63})', test_str)
    for item in mo:
        print(item)


if __name__ == '__main__':
    test_one()
