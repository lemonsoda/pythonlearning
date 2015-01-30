#!/usr/bin/python
#coding=utf8
 
import httplib
 
httpClient = None
 
try:
    httpClient = httplib.HTTPConnection('www.douban.com', 80, timeout=30)
    
    headers={'User-Agent':'Mozilla/6.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'}
    #headers['Cookie']=r'dbcl2="87827003:qwtEj15liGo"'
    httpClient.request('GET', '/accounts/',None,headers)
    
    #response是HTTPResponse对象
    response = httpClient.getresponse()
    print response.status
    print response.reason
    print response.read()
    print response.getheaders()
except Exception, e:
    print e
finally:
    if httpClient:
        httpClient.close()
