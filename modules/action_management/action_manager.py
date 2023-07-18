from modules.natural_language_processing import NaturalLanguageProcessor, ActionLabel
from .weather import WeatherHandler
from .joke import JokeHandler


class ActionManager:
    def __init__(self, language: str):
        self.natural_language_processor = NaturalLanguageProcessor(language)
        self.weather_handler = WeatherHandler()
        self.joke_handler = JokeHandler(language)

    def act(self, prompt: str) -> str:
        # TODO correct error when sending NONE into prompt (try catch)
        action_label = self.natural_language_processor.process(prompt)

        result = 'I did not understand the question or I do not support this functionality, Sir'

        match action_label:
            case ActionLabel.GET_WEATHER.value:
                # TODO : Add possibility to choose the location and time of the weather
                result = self.weather_handler.get_weather("Charleroi")
            case ActionLabel.GET_JOKE.value:
                # TODO : Add the possibility to choose the category of the jokes
                result = self.joke_handler.get_joke()

        return result

