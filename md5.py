import sys

filename = sys.argv[1]
f = open(filename, "rb")
data = f.read()


import hashlib

h = hashlib.md5()
h.update(data)
print(h.hexdigest())
