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

                return response.json()
