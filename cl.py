import sys
import urllib.request
import json


# 뒤에 차례대로 오는 인자들을 받아 virustotal~ URL 만들기
api = sys.argv[1]
rs = sys.argv[2]
site = "http://www.virustotal.com/vtapi/v2/file/report?apikey=%s&resource=%s" % (api,rs)


# URL 웹 요청을 하여 json 형식으로 돌려받기 
a = urllib.request.urlopen(site)
data = a.read().decode('utf-8')


# json 사용하여 문자열을 json 개체로 변환!
data2 = json.loads(data)
data3 = data2['scans']


# 키와 값을 분류하여 'detected' = True 인거 개수 세기!
count=0
for i,j in data3.items():
	print('key : ' , i)
	print('value :' , j)
	if j['detected'] == True :
		count += 1
		print(count)
