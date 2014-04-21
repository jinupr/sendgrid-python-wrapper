# -*- coding: utf-8 -*-

#########################################################################
#    FileName : sengridagent.py
#    Sendgrid Client Object for SendGrid
#    Author: Jinu P R
#    CopyRight: My Parichay 2014. All Rights Reserved
#########################################################################

import sys
import requests
from socket import timeout

from sendgrid import SendGridClient


class SendGridClient(SendGridClient):
    def __init__(self,username,password,**opts):
        super(SendGridClient, self).__init__(username, password, **opts)

    def _build_body(self,data):
        if sys.version_info < (3,0):
            for k in data.possible_values:
                v = getattr(data, k)
                if isinstance(v, unicode):
                    setattr(data, k, v.encode('utf-8'))
        values = {
                    'api_user':self.username,
                    'api_key' : self.password
                }
        for each in data.possible_values:
            values[each] = getattr(data,each)
        
        for k in list(values.keys()):
            if not values[k]:
                del values[k]
        return values
    def _make_request(self, data):
        data_to_send = self._build_body(data)
        headers = {'content-type':'application/x-www-form-urlencoded'}
        r = requests.get(self.mail_url,params=data_to_send,headers=headers)
        return r.status_code , r.content

    def send(self, data):
        if self._raise_errors:
            return self._raising_send(data)
        else:
            return self._legacy_send(data)

    def _legacy_send(self, data):
        try:
            return self._make_request(data)
        except HTTPError as e:
            return e.code, e.read()
        except timeout as e:
            return 408, e

    def _raising_send(self, data):
        try:
            self._make_request(data)
        except HTTPError as e:
            if e.code in range(400, 500):
                raise SendGridClientError(e.code, e.read())
            elif e.code in range(500, 600):
                raise SendGridServerError(e.code, e.read())
            else:
                assert False
        except timeout as e:
            raise SendGridClientError(408, 'Request timeout')

    
