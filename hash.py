import hashlib

m = hashlib.md5()
m.update(b"abc")
print(m.hexdigest())
