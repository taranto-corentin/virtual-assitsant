import logging

from modules.speech_recognizer import SpeechRecognizer


def start_log():
    logging.info("====================================================================================================")
    logging.info("                                          NEW RUN                                                   ")
    logging.info("====================================================================================================")


if __name__ == '__main__':
    # Creation of the log file
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        filename='app.log',
        filemode='a'
    )

    # Do the speech recognition
    speech_recognizer = SpeechRecognizer()
    text = speech_recognizer.recognize_speech()
    print(text)

