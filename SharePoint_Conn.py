import requests
import os
from requests_ntlm import HttpNtlmAuth
from urllib.error import HTTPError
import argparse
import base64
import urllib3


user_credentials={
    'username':'user',
    'password':'pass',
    'domain':''
}

class UserAuthentication:
    def __init__(self, username, password, domain, flm_url, flm_file):
        self.__username = username
        self.__password = password
        self.__domain = domain
        self.__flm_url = flm_url
        self.__ntlm_auth = None
        self.__flm_file = flm_file

    def authenticate(self):
        login_user = self.__domain + "\\" + self.__username
        user_auth = HttpNtlmAuth(login_user, self.__password)
        self.__ntlm_auth = user_auth


        my_headers = {
            'accept' : 'application/json;odata=verbose',
            'content-type' : 'application/json;odata=verbose',
            'odata' : 'verbose',
            'X-RequestForceAuthentication' : 'true'
        }

        try:
            result = requests.get(self.__flm_url, auth=user_auth, headers=my_headers, verify=False)
            f = self.__flm_output_filename
            print(result.status_code)

            if result.status_code == 200:
                with open(f, 'wb') as f:
                    output = f.write(result.content)

        except HTTPError as e:
            pass
        if result.status_code == requests.codes.ok:
            return  True
        


if __name__=="__main__":
    username = user_credentials['username']
    password = user_credentials['password']
    domain = user_credentials['domain']

    flm_url = f"<Your sharepoint-site-file-url>"
    flm_file = os.path.join('C:/Users/Ganesh/files')
    auth_object = UserAuthentication(username,password,domain,flm_url, flm_file)
    result = auth_object.authenticate()

    if result :
        print("Successfully login to site")