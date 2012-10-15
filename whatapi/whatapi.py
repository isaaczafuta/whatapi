from ConfigParser import ConfigParser
import json
import requests

headers = {
    'Content-type': 'application/x-www-form-urlencoded',
    'Accept-Charset': 'utf-8',
    'User-Agent': 'whatapi [isaaczafuta]'
    }

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
        loginpage = 'https://ssl.what.cd/login.php'
        data = {'username': self.username,
                'password': self.password,
                'keeplogged': 1,
                'login': 'Login'
        }
        r = self.session.post(loginpage, data=data, allow_redirects=False)
        if r.status_code != 302:
            raise LoginException
        accountinfo = self.request("index")
        self.authkey = accountinfo["response"]["authkey"]

    def request(self, action, **kwargs):
        '''Makes an AJAX request at a given action page'''
        ajaxpage = 'https://ssl.what.cd/ajax.php'
        params = {'action': action}
        if self.authkey:
            params['auth'] = self.authkey
        params.update(kwargs)

        r = self.session.get(ajaxpage, params=params, allow_redirects=False)
        try:
            if r.json["status"] != "success":
                raise RequestException
            return r.json
        except ValueError:
            raise RequestException