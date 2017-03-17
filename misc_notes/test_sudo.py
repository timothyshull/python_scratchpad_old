#!/opt/bin/python2.7

import os
import sys
import errno

try:
    fd = open('/etc/sudoers')
except IOError as e:
    print >> sys.stderr, 'in error'
    print >> sys.stderr, str(e[0])
    print >> sys.stderr, e.message
    if e[0] == errno.EPERM or e[0] == errno.EACCES:
        print >> sys.stderr, "You need root permissions to do this"
        sys.exit(1)
