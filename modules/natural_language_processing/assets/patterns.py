from modules.natural_language_processing.action_label import *


patterns = [
    {"label": ActionLabel.GET_WEATHER.value, "pattern": [{"LOWER": "weather"}, {"LOWER": "like"}]},
    {"label": ActionLabel.GET_WEATHER.value, "pattern": [{"LOWER": "weather"}, {"LOWER": "report"}]},
    {"label": ActionLabel.GET_JOKE.value, "pattern": [{"LOWER": "joke"}]},
    {"label": ActionLabel.GET_JOKE.value, "pattern": [{"LOWER": "laugh"}]},
]