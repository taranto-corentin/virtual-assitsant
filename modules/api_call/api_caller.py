from typing import Optional

import requests

from modules.api_component.api_method import ApiMethod


class ApiCaller:
    def __init__(self, url: str, method: ApiMethod):
        self.headers = self.create_headers()
        self.url = url
        self.method = method

    def create_headers(self) -> dict:
        return {'accept': 'application/json'}

    def call(self, query_parameters: Optional[str]):
        match self.method:
            case ApiMethod.GET:
                response = requests.get(self.url + query_parameters, self.headers)

                status_code = response.status_code

                if 200 <= status_code < 300:
                    return response.json()
                elif 400 <= status_code < 500:
                    # TODO : Add error handling to make the assistant say there is a problem
                    return 'An error occurred client side'
                elif 500 <= status_code < 600:
                    return 'An error occurred server side'
