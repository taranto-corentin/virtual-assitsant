import pyjokes
import logging

from pyjokes.pyjokes import LanguageNotFoundError, CategoryNotFoundError


# TODO : Check for a better library than pyjokes because doesn't seem really good
class JokeHandler:
    def __init__(self, language: str):
        logging.info(f'Joke handler creation (language = {language})')

        self.language = language.lower()

    def get_joke(self):
        try:
            joke = pyjokes.get_joke(language=self.language)

            return joke
        except LanguageNotFoundError as e:
            logging.error(f'Error occurred in JokeHandler.get_joke() : {e.__str__()}')

            return 'Sorry, I do not know any joke in your language'

    def get_joke_by_category(self, category: str):
        try:
            joke = pyjokes.get_joke(language=self.language, category=category)

            return joke
        except LanguageNotFoundError as e:
            logging.error(f'Error occurred in JokeHandler.get_joke() : {e.__str__()}')

            return 'Sorry, I do not know any joke in your language'
        except CategoryNotFoundError as e:
            logging.error(f'Error occurred in JokeHandler.get_joke() : {e.__str__()}')

            return 'Sorry, I do not have any joke for the category you asked'
