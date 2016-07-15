#not really fix utf8 problem
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

#not really fix utf8 problem
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#get html source
url = 'http://rate.bot.com.tw/Pages/Static/UIP003.zh-TW.htm'
#rs = requests.session()
#r = rs.get(url)
r = requests.get(url)
#requests.setCharacterEncoding("UTF-8");
#r.text.encode("utf-8")
print r.text

#save to file
data = open('data.html', 'w')
data.write(r.text)
data.close()
