import logging

from dotenv import load_dotenv

from config import ConfigReader
from modules.action_management import ActionManager
from modules.dialogue_management.assets.texts import *
from modules.speech_recognizer import SpeechRecognizer
from modules.text_to_speech import TextToSpeech


def start_log():
    logging.info("====================================================================================================")
    logging.info("                                          NEW RUN                                                   ")
    logging.info("====================================================================================================")


if __name__ == '__main__':
    # Load the data from the .env file at the root of the project
    load_dotenv()

    # Get the config
    config = ConfigReader()

    # Creation of the log file
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filename='app.log',
        filemode='a'
    )

    start_log()

    # Do the text to speech
    tts = TextToSpeech(config.language)

    tts.read(DIALOGUE_HELLO_TEXT)

    # Do the speech recognition
    speech_recognizer = SpeechRecognizer(config.language)
    text = speech_recognizer.recognize_speech()
    print(text)

    # Do the required action
    action_manager = ActionManager(config.language)
    response = action_manager.act(text)

    tts.read(response)

