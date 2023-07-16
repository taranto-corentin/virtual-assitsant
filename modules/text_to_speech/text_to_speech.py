import logging
import os

import pygame.mixer


class TextToSpeech:
    def __init__(self, language: str):
        pygame.mixer.init()

        self.language = language.lower()
        self.voice = self.get_voice(language)

    def get_voice(self, language: str) -> str:
        match language:
            case 'FR':
                return 'fr-FR-HenriNeural'
            case 'EN':
                return 'en-US-SteffanNeural'

        return 'en-US-SteffanNeural'

    def read(self, text: str):
        command = f'edge-tts --voice "{self.voice}" --text "{text}" --write-media "output.mp3"'

        os.system(command)

        pygame.mixer.init()

        pygame.mixer.music.load("output.mp3")

        try:
            pygame.mixer.music.play()

            clock = pygame.time.Clock()

            while pygame.mixer.music.get_busy():
                clock.tick(10)
        except Exception as e:
            logging.error(f'An error occurred while playing the text to speech file : {e}')
        finally:
            pygame.mixer.music.stop()
            pygame.mixer.quit()
