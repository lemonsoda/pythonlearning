#!/usr/bin/python

import json
import httplib
import urllib
class Login(object):
    
    def login(self):
        accinfo=self.getaccount()
        self.dologin(accinfo)
        
    def getaccount(self):
        with open('account','rb') as f:
            jsonstr=f.read()
            accountinfo=json.loads(jsonstr)
            return accountinfo

    def dologin(self,accinfo):
        httpClient = None
        try:
            httpClient = httplib.HTTPConnection('www.douban.com', 80, timeout=30)
            accinfo['source']='index_nav'
            body=urllib.urlencode(accinfo)
            headers={
                'User-Agent':'Mozilla/6.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36',
                'Content-Type':'application/x-www-form-urlencoded',
                'Accept-Encoding':'gzip, deflate',
                'Cache-Control':'max-age=0',
                'Connection':'keep-alive',
                'Content-Length':str(len(body)),
                'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4',
                'Host':'www.douban.com',
                'Origin':'http://www.douban.com',
                'Referer':'http://www.douban.com/'
                }
            
            httpClient.request('POST', 'https://www.douban.com/accounts/login',body,headers)
            
            response = httpClient.getresponse()
            print response.status
            print response.reason
            print response.getheaders()
            print '-----------html body---------'
            print response.read()
        except Exception, e:
            print e
        finally:
            if httpClient:
                httpClient.close()
        
        
if __name__=='__main__':
    Login().login()
        
