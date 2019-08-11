import json
import requests


class RescaleApi:

    ENDPOINT = 'https://platform.rescale.com/api'
    VERSION = 'v2'

    def __init__(self, api_secret):
        self.api_secret = api_secret

    def request(self, search, data=None, http_method='GET'):
        """
            methods - List of methods to be joined, e.g. ['events', 'properties', 'values']
                      will give us http://mixpanel.com/api/2.0/events/properties/values/
            params - Extra parameters associated with method
        """

        endpoint = self.ENDPOINT
        request_url = '/'.join([endpoint, str(self.VERSION)]) + '/' + search
        headers = {'Authorization': 'Token {}'.format(self.api_secret)}
        if http_method == 'GET':
            response = requests.get(request_url, headers=headers)
            print(request_url)
        elif http_method == 'POST':
            response = requests.post(request_url, headers=headers, files=data)
            print(request_url)
        return json.loads(response._content)
