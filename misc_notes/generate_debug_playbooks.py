import os
import glob
import yaml
import re

from ansible.utils.unicode import to_unicode
from ansible.parsing.yaml.dumper import AnsibleDumper

def to_playbook_yaml(a, *args, **kwargs):
    transformed = yaml.dump(a,
                            Dumper=AnsibleDumper,
                            indent=2,
                            allow_unicode=True,
                            default_flow_style=False,
                            width=320,
                            **kwargs)
    return to_unicode(transformed)


def write_debug_playbook(input_file):
    pb_yaml = yaml.safe_load(open(input_file))

    for play in pb_yaml:
        play['strategy'] = 'debug'

    mo = re.search('(.*)\.yml', input_file)
    output_filename = '{0}-debug.yml'.format(mo.group(1))

    with open(output_filename, 'w+') as f:
        f.write('---\n')
        f.write(to_playbook_yaml(pb_yaml))


def main():
    all_playbooks = glob.glob('{0}/playbooks/*.yml'.format(ANSIBLE_PATH)) + \
                    glob.glob('{0}/playbooks/dev_cmd/*.yml'.format(ANSIBLE_PATH))
    all_playbooks = [elem for elem in all_playbooks if 'debug' not in elem]
    for playbook in all_playbooks:
        write_debug_playbook(playbook)


if __name__ == '__main__':
    main()
