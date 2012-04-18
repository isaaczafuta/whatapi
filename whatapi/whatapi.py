from ConfigParser import ConfigParser
import json
import requests

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3)'\
        'AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.79'\
        'Safari/535.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9'\
        ',*/*;q=0.8',
    'Accept-Encoding': 'gzip,deflate,sdch',
    'Accept-Language': 'en-US,en;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3'}


class LoginException(Exception):
    pass


class RequestException(Exception):
    pass


class WhatAPI:
    def __init__(self, config=None, username=None, password=None):
        self.session = requests.session(headers=headers)
        self.authkey = None
        if config:
            config = ConfigParser()
            config.read(config)
            self.username = config.get('login', 'username')
            self.password = config.get('login', 'password')
        else:
            self.username = username
            self.password = password
        self._login()

    def _login(self):
        '''Logs in user and gets authkey from server'''
        loginpage = 'http://what.cd/login.php'
        data = {'username': self.username,
                'password': self.password}
        r = self.session.post(loginpage, data=data)
        if r.status_code != 302 or r.headers['location'] != 'index.php':
            raise LoginException
        accountinfo = self.request("index")
        self.authkey = accountinfo["response"]["authkey"]

    def request(self, action, **kwargs):
        '''Makes an AJAX request at a given action page'''
        ajaxpage = 'http://what.cd/ajax.php'
        params = {'action': action}
        if self.authkey:
            params['auth'] = self.authkey
        params.update(kwargs)
        r = self.session.get(ajaxpage, params=params)
        try:
            parsed = json.loads(r.content)
            if parsed["status"] != "success":
                raise RequestException
            return parsed
        except ValueError:
            raise RequestException
