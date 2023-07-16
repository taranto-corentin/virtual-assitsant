from modules.natural_language_processing import NaturalLanguageProcessor, ActionLabel
from .weather import WeatherHandler


class ActionManager:
    def __init__(self, language: str):
        self.natural_language_processor = NaturalLanguageProcessor(language)
        self.weather_handler = WeatherHandler()

    def act(self, prompt: str) -> str:
        # TODO correct error when sending NONE into prompt (try catch)
        action_label = self.natural_language_processor.process(prompt)

        result = 'I did not understand the question or I do not support this functionality, Sir'

        match action_label:
            case ActionLabel.GET_WEATHER.value:
                result = self.weather_handler.get_weather("Charleroi")

        return result

