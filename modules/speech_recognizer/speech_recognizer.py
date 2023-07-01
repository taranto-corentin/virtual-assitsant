import speech_recognition as sr
import logging


class SpeechRecognizer:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def recognize_speech(self):
        with sr.Microphone() as source:
            audio = self.recognizer.listen(source)

        logging.error("Test")

        try:
            text = self.recognizer.recognize_google(audio, language="fr-FR")

            return text
        except sr.UnknownValueError:
            logging.error("Unable to recognize speech.")

            return None
        except sr.RequestError as e:
            logging.error(f"Error occurred during the speech recognition : {e}")

            return None
