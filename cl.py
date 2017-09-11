import sys
import urllib.request
import json
import re

# 뒤에 차례대로 오는 인자들을 받아 virustotal~ URL 만들기
api = sys.argv[1]
rs = sys.argv[2]
site = "http://www.virustotal.com/vtapi/v2/file/report?apikey=%s&resource=%s" % (api,rs)

# URL 웹 요청을 하여 json 형식으로 돌려받기 
a = urllib.request.urlopen(site)
data = a.read()
encoding = a.info().get_content_charset('utf8')
data2 = str(json.loads(data.decode(encoding)))

# 돌려받은 것을 정규식 표현으로 걸러내기
p = re.compile("'detected': True")
m = p.search(data2)
print(m.group(0))
print(m.group(1))
