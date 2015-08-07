__author__ = 'chexiaoyu'
#coding:utf-8

import spider_class
import urllib2
import urllib
import json
import re
import requests


class API_process:


    def __init__(self,access_token):
        self.access_token = access_token
        self.url = 'http://dev02.haizhi.com:19977/'


    def Get_access_token(self):
        dir = 'api/opends_token/gen'
        values = {"access_token":self.access_token}
        data = urllib.urlencode(values)
        request = urllib2.Request(self.url + dir,data)
        response = urllib2.urlopen(request)
        js = response.read()
        js = json.loads(js)
        #js = json.loads(response.read())
        self.access_token = js["result"]["access_token"]


    def Create_database(self,database_name):
        dir = 'api/ds/create'
        values = {"access_token":self.access_token,"name":database_name,"type":"opends"}
        data = urllib.urlencode(values)
        request = urllib2.Request(self.url + dir,data)
        response = urllib2.urlopen(request)
        js = json.loads(response.read())
        if js["status"] == "0":
            print "数据库创建成功！"
        else:
            print js["errstr"]


    def Show_database(self):
        dir = 'api/ds/list'
        values = {"access_token":self.access_token}
        data = urllib.urlencode(values)
        request = urllib2.Request(self.url + dir,data)
        response = urllib2.urlopen(request)
        js = json.loads(response.read())
        if js["status"] == "0":
            print js["result"]["data_source"][1]["ds_id"]
        else:
            print js["errstr"]

#error
    def Del_database(self,ds_id):
        dir = 'api/ds/delete'
        values = {"access_token":self.access_token,"ds_id":ds_id}
        data = urllib.urlencode(values)
        request = urllib2.Request(self.url + dir,data)
        response = urllib2.urlopen(request)
        js = json.loads(response.read())
        if js["status"] == "0":
            print "指定数据库删除成功！"
        else:
            print js["errstr"]



#   def Create_table(self):
#        dir = 'api/tb/create'



access_token = "0a27d480339ebe12e8f0f09f1bcf0d97"
process = API_process(access_token)
process.Get_access_token()
#process.Create_database("test1")
#process.Show_database()
#process.Del_database('ds_d3ff549bb4dd4b5f8b67c3eceef635d3')
#print process.access_token
#print process.Get_access_token(access_token)

