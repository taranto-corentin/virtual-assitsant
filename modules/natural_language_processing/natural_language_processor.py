import spacy

from modules.natural_language_processing.assets.patterns import patterns


class NaturalLanguageProcessor:
    def __init__(self, language: str):
        # Load the model for the language specified
        self.nlp = spacy.load('en_core_web_sm')
        self.matcher = spacy.matcher.Matcher(self.nlp.vocab)

        self.load_patterns()

    def load_patterns(self):
        for pattern in patterns:
            self.matcher.add(pattern['label'], [pattern['pattern']])

    def process(self, text: str):
        processed_text = self.nlp(text)

        matches = self.matcher(processed_text)

        if matches:
            for match_id,  start, end in matches:
                matched_label = self.nlp.vocab.strings[match_id]

                print(matched_label)

                return matched_label
