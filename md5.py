import sys
import hashlib

# 파일 이름 받아오기
filename = sys.argv[1]
f = open(filename, "rb")
data = f.read()


# 받아온 파일에 대한 해시값 구하기
h = hashlib.md5()
h.update(data)
print(h.hexdigest())

