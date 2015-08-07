__author__ = 'chexiaoyu'

import urllib
import urllib2
import httplib
import json
import re

# #test httplib
# conn = httplib.HTTPSConnection('http://dev02.haizhi.com:19977')
# #parm = '0a27d480339ebe12e8f0f09f1bcf0d97'
#
# conn.request('POST','/api/open/token_gen?access_token=0a27d480339ebe12e8f0f09f1bcf0d97')
# res = conn.getresponse().read()
# res = json.loads(res)
# print res


access_token = "0a27d480339ebe12e8f0f09f1bcf0d97"
url = 'http://dev02.haizhi.com:19977/api/opends_token/gen'
#url = 'https://open.bdp.cn/'
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.130 Safari/537.36"
#headers = {'User-Agent':user_agent}
values = {"access_token":access_token}
data = urllib.urlencode(values)
request = urllib2.Request(url,data)
response = urllib2.urlopen(request)
js = response.read()
#print "access_token = ",dict["result"]
js = json.loads(js)
print js
print js["result"]["access_token"]
