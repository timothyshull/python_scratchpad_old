import socket
import os

home = os.path.expanduser('~')
print home
test_val = socket.gethostbyname('www.google.com')
print test_val
