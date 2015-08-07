#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import requests
import time
from requests.exceptions import ConnectionError
#from util.logger import error_logger


def enum(**enums):
    return type('Enum', (), enums)


def singleton(cls, *args, **kw):
    instances = {}

    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]

    return _singleton


class OpenDSException(Exception):
    pass


class OpenDS():
    """
    OpenDS交互模块
    """

    def __init__(self):
        self.url_prefix = 'http://dev02.haizhi.com:19977/api'

    def _request(self, url, payload):
        res = None
        try_count = 0
        while True:
            try:
                res = requests.post(url, data=payload)
                break
            except ConnectionError as e:
                try_count += 1
                print 'can not connect to tassadar, retry ...'
                time.sleep(15)
                if try_count == 5:
                    raise e
        result = res.json()
        if result['status'] != '0':
            error_logger().info("[%s]:[%s]"%(url,result['errstr']))
            raise OpenDSException(result['errstr'])
        return result['result']

    def ds_create(self, token, name):
        url = '%s/ds/create' % self.url_prefix
        params = {
            'access_token': token,
            'name': name,
            'type': 'opends'
        }
        return self._request(url, params)

    def ds_list(self, token):
        url = '%s/ds/list' % self.url_prefix
        params = {
            'access_token': token
        }
        return self._request(url, params)

    def ds_delete(self, token, ds_id):
        url = '%s/ds/list' % self.url_prefix
        params = {
            'access_token': token,
            'ds_id': ds_id
        }
        return self._request(url, params)

    def tb_create(self, token, ds_id, name, data, uniq_key):
        url = '%s/tb/create' % self.url_prefix
        params = {
            'access_token': token,
        }
        data = {
            'ds_id': ds_id,
            'name': name,
            'schema': data,
            'uniq_key': uniq_key
        }
        print data
        res = requests.post(url, params=params, data=json.dumps(data)).json()
        if res['status'] != '0':
            error_logger().info(res['errstr'])
            raise OpenDSException(res['errstr'])
        else:
            return res['result']

    def tb_list(self, token, ds_id):
        url = '%s/tb/list' % self.url_prefix
        params = {
            'access_token': token,
            'ds_id': ds_id
        }
        return self._request(url, params)

    def tb_clean(self, token, tb_id):
        url = '%s/tb/clean' % self.url_prefix
        params = {
            'access_token': token,
            'tb_id': tb_id
        }
        return self._request(url, params)

    def tb_write(self, token, tb_id, data):
        url = '%s/tb/write' % self.url_prefix
        params = {
            'access_token': token,
            'tb_id': tb_id
        }
        data = {'data': data}
        res = requests.post(url, params=params, data=json.dumps(data)).json()
        if res['status'] != 0:
            error_logger().info(res['errstr'])
            raise OpenDSException(res['errstr'])
        else:
            return res['result']

    def tb_merge(self, token, tb_id):
        url = '%s/tb/commit' % self.url_prefix
        params = {
            'access_token': token,
            'tb_id': tb_id
        }
        return self._request(url, params)

    def tb_update(self, token, tb_ids):
        url = '%s/tb/update' % self.url_prefix
        params = {
            'access_token': token,
            'tb_ids': json.dumps(tb_ids)
        }
        return self._request(url, params)

    def data_delete(self, token, tb_id, fields, data):
        url = '%s/data/delete' % self.url_prefix
        params = {
            'access_token': token,
            'tb_id': tb_id,
            'fields': json.dumps(fields)
        }
        data = map(lambda x: x.encode(''), data)
        data = {'data': data}
        return requests.post(url, params=params, data=json.dumps(data)).json()

    def tb_insert(self, token, tb_id, fields, data):
        url = '%s/tb/insert' % self.url_prefix
        params = {
            'access_token': token,
            'tb_id': tb_id,
            'fields': json.dumps(fields)
        }
        res = requests.post(url, params=params, data=json.dumps(data))
        res = res.json()
        if res['status'] != '0':
            error_logger().info(res['errstr'])
            raise OpenDSException(res['errstr'])
        else:
            return res['result']

    def field_list(self, token, tb_id):
        url = '%s/field/list' % self.url_prefix
        params = {
            'access_token': token,
            'tb_id': tb_id
        }
        return self._request(url, params)

    def field_del(self, token, tb_id, name):
        url = '%s/field/delete' % self.url_prefix
        params = {
            'access_token': token,
            'tb_id': tb_id,
            'name': name
        }
        return self._request(url, params)

    def field_add(self, token, tb_id, name, type, uniq_index):
        url = '%s/field/add' % self.url_prefix
        params = {
            'access_token': token,
            'tb_id': tb_id,
            'name': name,
            'type': type,
            'uniq_index': uniq_index
        }
        return self._request(url, params)

    def field_modify(self,token, tb_id, name, type, uniq_index):
        url = '%s/field/modify' % self.url_prefix
        params = {
            'access_token': token,
            'tb_id': tb_id,
            'name': name,
            'type': type,
            'uniq_index': uniq_index
        }
        return self._request(url, params)