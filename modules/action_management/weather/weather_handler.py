import os
from typing import Optional

from modules.api_call import ApiCaller
from modules.api_component import EndpointName, ApiMethod


# TODO : Add analysis of the weather in order to guess if it will rain or not through machine learning
class WeatherHandler:
    def __init__(self):
        pass

    def get_weather(self, location: str):
        api_caller = ApiCaller(str(EndpointName.TOMORROW_GET_WEATHER.value), ApiMethod.GET)
        query_parameter = self.create_get_weather_query_parameters(location, "1d")
        weather_data = api_caller.call(query_parameter)

        target_weather_data = weather_data['timelines']['daily'][0]['values']

        return f'The temperature today is {target_weather_data["temperatureAvg"]} degree Celcius'

    def create_get_weather_query_parameters(self, location: str, timesteps: Optional[str]):
        query_parameter = f'location={location}&'

        if timesteps:
            query_parameter += f'timesteps={timesteps}&'

        query_parameter += f'apikey={os.getenv("TOMORROW_IO_API_KEY")}'

        return query_parameter
