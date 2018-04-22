# -*- coding: utf-8 -*-

def dict2list(dic:dict):
    keys = dic.keys()
    vals = dic.values()
    lst = [(key, val) for key, val in zip(keys, vals)]
    return lst

def load():
    url_list = [['InfoQ', 'http://mp.weixin.qq.com/profile?src=3&timestamp=1498483386&ver=1&signature=33uh3zsZYPHNwW6fGu*vFp3FE0rOMtA82o8ZUHSy4Gy329ihc4QZjbgtdVLEGlXOkzpjXEp3mvkt1TRLtQMH8g=='],
                ['经管之家论坛', 'http://mp.weixin.qq.com/profile?src=3&timestamp=1498483970&ver=1&signature=ggg-z0xyYrYzwI-5XrLz-*aLiXbmfCOJGkbWYLm3phoV5n51hDqEESBmOZoOIsYvsFWOWB8NhnqB7-P7qTD82Q=='],
                ['warfalcon', 'http://mp.weixin.qq.com/profile?src=3&timestamp=1498484401&ver=1&signature=KA*MA80TrZNv1XLa9hRMDtfuyVnn4ndT9r2VqyA6n1NOQDrmVHATgz7jRoHIzOBL7qREFs8QvI7hn-xvWQXznw==']
                ]
    return url_list
