import sys

api = sys.argv[1]
rs = sys.argv[2]




site = "http://www.virustotal.com/vtapi/v2/file/report?apikey=%s&resource=%s" % (api,rs)
print(site)



