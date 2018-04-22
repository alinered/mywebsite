# -*- coding: utf-8 -*-

def load():
    html = '<html><head><meta name="viewport" content="width=device-width,minimum-scale=1.0,maximum-scale=1.0" /><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><link href="enrollment2.css" rel="stylesheet" type="text/css" /><script src="jquery.min.js"></script><title>mywebsite</title></head><meta http-equiv="Content-type" name="viewport" content="initial-scale=1.0, maximum-scale=1.0, user-scalable=no, width=device-width"><style type="text/css">body{text-align:center;background:url("http://img2.niutuku.com/desk/1207/1035/ntk119739.jpg") no-repeat;}a:link,a:visited{text-decoration:none;}a:hover{text-decoration:underline;}</style>'
    bookmark_list = [['百度', 'https://www.baidu.com'],
                     ['知乎日报', 'zhihudaily'],
                     ['Inoreader', 'https://www.inoreader.com'],
                     ['QQ邮箱', 'https://mail.qq.com'],
                     ['古典音乐频道', 'http://www.ncpa-classic.com'],
                     ['网易云音乐', 'https://music.163.com'],
                     ['虾米音乐', 'https://www.xiami.com'],
                     ['豆瓣电影', 'https://movie.douban.com'],
                     ['id97', 'http://www.id97.com'],
                     ['kindle推', 'http://www.kindlepush.com/main']
                     ]
    for i in bookmark_list:
        html += '<a href="%s" target="_blank">%s</a><br>'% (i[1], i[0])
    html += '</html>'
    return html
