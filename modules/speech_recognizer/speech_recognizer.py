import speech_recognition as sr
import logging


class SpeechRecognizer:
    def __init__(self, language: str):
        self.recognizer = sr.Recognizer()
        self.language = self.format_language(language)

    def format_language(self, language: str) -> str:
        match language:
            case 'FR':
                return 'fr-FR'
            case 'EN':
                return 'en-US'

        return 'en-US'

    def recognize_speech(self):
        with sr.Microphone() as source:
            audio = self.recognizer.listen(source)

        logging.error('Test')

        try:
            text = self.recognizer.recognize_google(audio, language=self.language)

            return text
        except sr.UnknownValueError:
            logging.error('Unable to recognize speech.')

            return None
        except sr.RequestError as e:
            logging.error(f'Error occurred during the speech recognition : {e}')

            return None
