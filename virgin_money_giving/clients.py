import requests
from exceptions import NotImplementedError


class BaseAPIClient(object):
    base_url = 'https://api.virginmoneygiving.com/'
    api_path = None
    api_key = None
    headers = {
        'Accept': 'application/json'
    }

    def __init__(self, api_key, sandbox=False):
        self.api_key = api_key
        if not self.api_path:
            raise NotImplementedError(
                'BaseAPIClient subclasses must set "api_path"'
            )

    def get(self, method, params={}):
        params['api_key'] = self.api_key
        endpoint = self.base_url + self.api_path + method
        response = requests.get(
            endpoint,
            params=params,
            headers=self.headers,
        )
        response.raise_for_status()
        return response.json()


class FundraiserAPIClient(BaseAPIClient):
    api_path = 'fundraisers/v1/'

    def fundraiser_search(self, surname, forename=None):
        params = {}
        params['surname'] = surname
        if forename:
            params['forename'] = forename
        return self.get('search', params)

    def fundraiser_details(self, resource_id):
        return self.get(
            'account/{}'.format(resource_id)
        )

    def fundraiser_page_details(self, resource_id, page_id):
        return self.get(
            'account/{0}/pages/{1}'.format(resource_id, page_id)
        )
