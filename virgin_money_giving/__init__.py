import requests


class VirginMoneyGivingAPIClient(object):
    base_url = 'https://api.virginmoneygiving.com/'
    api_key = None
    headers = {
        'Accept': 'application/json'
    }

    def __init__(self, api_key, sandbox=False):
        self.api_key = api_key

    def get(self, method, params={}):
        params['api_key'] = self.api_key
        endpoint = self.base_url + method
        response = requests.get(
            endpoint,
            params=params,
            headers=self.headers,
        )
        response.raise_for_status()
        return response.json()

    def post(self, method, data, params={}):
        # TODO
        raise NotImplementedError()

    def fundraiser_search(self, surname, forename=None):
        params = {}
        params['surname'] = surname
        if forename:
            params['forename'] = forename
        return self.get('fundraisers/v1/search', params)

    def fundraiser_details(self, resource_id):
        return self.get(
            'fundraisers/v1/account/{0}'.format(resource_id)
        )

    def fundraiser_page_details(self, resource_id, page_id):
        return self.get(
            'fundraisers/v1/account/{0}/pages/{1}'.format(resource_id, page_id)
        )

    def charity_search(self):
        # TODO
        raise NotImplementedError()

    def validate_url(self):
        # TODO
        raise NotImplementedError()

    def country_code_lookup(self):
        # TODO
        raise NotImplementedError()   

    def address_lookup(self):
        # TODO
        raise NotImplementedError()   
    
    def account_exists(self, email_address, date_of_birth):
        params = {}
        params['emailAddress'] = email_address
        params['dateOfBirth'] = date_of_birth
        return self.get(
            'fundraisers/v1/validateaccount.json', params
        )

    def create_fundraiser_account(self):
        # TODO
        raise NotImplementedError()

    def activity_lookup(self):
        # TODO
        raise NotImplementedError()

    def event_search(self):
        # TODO
        raise NotImplementedError()

    def event_summary(self):
        # TODO
        raise NotImplementedError()

    def event_fundraisers(self):
        # TODO
        raise NotImplementedError()

    def event_fundraisers_2(self):
        # TODO
        raise NotImplementedError()

    def charity_fundraisers(self):
        # TODO
        raise NotImplementedError()

    def charity_details(self):
        # TODO
        raise NotImplementedError()


