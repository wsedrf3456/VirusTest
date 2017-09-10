import sys
import hashlib

filename = sys.argv[1]
f = open(filename, "rb")
data = f.read()


h = hashlib.md5()
h.update(data)
print(h.hexdigest())
