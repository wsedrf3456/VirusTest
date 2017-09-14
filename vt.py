import sys
import urllib.request
import json
import hashlib


def hv():
	# 파일 이름 받아오기
	filename = sys.argv[2]
	f = open(filename, "rb")
	dt = f.read()

	# 받아온 파일에 대한 해시값 구하기
	h = hashlib.md5()
	h.update(dt)
	hashvalue = h.hexdigest()
	return hashvalue


# 뒤에 차례대로 오는 인자들을 받아 virustotal~ URL 만들기
api = sys.argv[1]
rs = hv()
site = "http://www.virustotal.com/vtapi/v2/file/report?apikey=%s&resource=%s" % (api,rs)


# URL 웹 요청을 하여 json 형식으로 돌려받기 
a = urllib.request.urlopen(site)
data = a.read().decode('utf-8')


# json 사용하여 문자열을 json 개체로 변환!
data2 = json.loads(data)
if data2['response_code'] == 0 :
	print("악성 코드 없음")
else: 
	data3 = data2['scans']

	# 키와 값을 분류하여 'detected' = True 인거 개수 세기!
	n=0
	count=0
	for i,j in data3.items():
		print(('%d 번째 엔진 : ' % n) , i)
		print('결과값 :' , j['detected'])
		n +=1
		if j['detected'] == True :
			count += 1
	print("총 %d 개의 엔진 중 %d 개가 악성이라 판단하였습니다." % (n,count))
