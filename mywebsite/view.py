# -*- coding: utf-8 -*-
from django.http import HttpResponse
import datetime
import time
from . import zhihudaily_page
from . import weixin_page
from . import bookmark_page

def index(request):
    html = bookmark_page.load()
    return HttpResponse(html)

def zhihudaily(request, param):
    #第一版的设计，只能显示前一天的知乎日报
    #yesterdayyear, yesterdaymonth, yesterdaydate = str(datetime.date.today() - datetime.timedelta(days=1)).split('-')
    #year, month, date = str(time.strftime("%Y-%m-%d", time.localtime())).split('-')
    
    yesterdayyear, yesterdaymonth, yesterdaydate = param[:4],param[4:6],param[6:]
    temp = datetime.datetime.strptime(param, "%Y%m%d").date() + datetime.timedelta(days=1)
    year, month, date = str(temp.year), str(temp.month), str(temp.day)
    month = month.zfill(2)
    date = date.zfill(2)
    
    msgtitle, msgurl = zhihudaily_page.load(year, month, date)
    num = len(msgtitle)
    now = yesterdayyear + '-' + yesterdaymonth + '-' + yesterdaydate
    html = '<html><head><meta name="viewport" content="width=device-width,minimum-scale=1.0,maximum-scale=1.0" /><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><link href="enrollment2.css" rel="stylesheet" type="text/css" /><script src="jquery.min.js"></script><title>zhihudaily</title></head><meta http-equiv="Content-type" name="viewport" content="initial-scale=1.0, maximum-scale=1.0, user-scalable=no, width=device-width"><style type="text/css">body{text-align:left;background:url("http://img2.niutuku.com/desk/1207/1035/ntk119739.jpg") no-repeat;}a:link,a:visited{text-decoration:none;}a:hover{text-decoration:underline;}</style><h1>%s</h1>' % now
    for i in range(num):
        #html += '<button type="button">Send Mail</button>  %-2d.<a href="%s" target="_blank">    %s</a><br>'% (i+1, msgurl[i], msgtitle[i])
        html += '%-2d.<a href="%s" target="_blank">    %s</a><br>'% (i+1, msgurl[i], msgtitle[i])
    html += '</html>'
    return HttpResponse(html)
