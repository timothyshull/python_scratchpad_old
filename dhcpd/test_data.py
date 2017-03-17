import os
import pprint
import re
import datetime
import time


class DHCPDParser(object):
    DEFAULT_TIME_FORMAT = '%H-%M_%m%d%Y'
    DEFAULT_FILENAME = 'dhcpd.leases'
    MAC_ADDRESS_RE = re.compile('((?:\w{2}:){5}\w{2})')
    IP_ADDRESS_RE = re.compile('((?:\d{1,3}\.){3}\d{1,3})')
    HOSTNAME_RE = re.compile('((?:[A-Za-z0-9\-_]{1,63}\.){2,63}[A-Za-z0-9\-_]{1,63})')

    def __init__(self, filename=None):
        super(DHCPDParser, self).__init__()
        self.time_stamp = None
        self.get_time_format()
        if os.path.exists(str(filename)):
            self.dhcp_file = filename
        elif os.path.exists(os.path.join(os.getcwd(), self.DEFAULT_FILENAME)):
            self.dhcp_file = os.path.abspath(os.path.join(os.getcwd(), self.DEFAULT_FILENAME))
        else:
            print('No file')
            exit(1)

        self.all_matches = None
        self.file_header = None
        self.errors = []
        self.get_entry_list()
        self.dhcpd_dictionary = {'hosts': None, 'leases': None}
        # self.build_dictionary()

    def get_time_format(self):
        # bugs here
        # self.time_stamp = datetime.datetime(time.time()).strftime(self.DEFAULT_TIME_FORMAT)
        pass

    def get_entry_list(self):
        try:
            with open(self.dhcp_file, 'r') as f:
                file_contents = f.read()
                self.file_header = file_contents.splitlines()[:3]
                self.all_matches = re.findall('\n([^\{|\n]*\{[^\}]+\})', file_contents, re.DOTALL | re.MULTILINE)
        except Exception as e:
            # TODO: add exception handling here
            pass

    def build_dictionary(self):
        for m in self.all_matches:
            if m.strip().startswith('host'):
                self.parse_single_host_match(m)
            if m.strip().startswith('lease'):
                self.parse_single_lease_match(m)

    def parse_single_host_match(self, m):
        split = m.splitlines()
        info_line = split[:1]
        # get hostname using host regex info_line[0]
        hostname = self.HOSTNAME_RE.search(info_line)
        # get other info from the block
        # using for in loop
        block = split[1:]
        host_dict = {
            'ip': '172.22.22.32', # sub value here
            'mac': '3h:32:...',
            'hostname': {
                'short': 'testhost',
                'full': 'teshost.com'
            }
        }

        print(info_line)
        print(block)
        self.dhcpd_dictionary['hosts'][hostname] = host_dict

    @staticmethod
    def parse_single_lease_match(m):
        split = m.splitlines()
        info_line = split[:1]
        block = split[1:]
        # self.dhcpd_dictionary['leases'][key] = value_dict
        if hostname:
            lease_dict['hostname'] = hostname


def main():
    parser = DHCPDParser()
    parser.build_dictionary()
    print(parser.dhcpd_dictionary)






if __name__ == '__main__':
    main()
