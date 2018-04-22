# -*- coding: utf-8 -*-
import re
import urllib.request

def load(year, month, date):
    urladd = year + month + date
    urlhead = 'http://news.at.zhihu.com/api/3/news/before/'
    url = urlhead + urladd

    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.8.1.14) Gecko/20080404 (FoxPlus) Firefox/2.0.0.14'
    headers = { 'User-Agent' : user_agent }
    req = urllib.request.Request(url, headers = headers)
    myResponse = urllib.request.urlopen(req)
    myPage = myResponse.read()
    myPage = myPage.decode('utf-8')
    #unicodePage = myPage.decode("utf-8")
    p1 = re.compile(r"id\":\d+")
    p2 = re.compile(r"title\":\".+?\"")
    readtitle = []
    #readid = []
    readurl = []
    #[readid.append(i[4:]) for i in p1.findall(myPage)]
    [readurl.append("http://daily.zhihu.com/story/" + i[4:]) for i in p1.findall(myPage)]
    [readtitle.append(i[8:-1]) for i in p2.findall(myPage)]
    #[readurl.append("http://daily.zhihu.com/story/" + i) for i in readid]
    return readtitle, readurl
