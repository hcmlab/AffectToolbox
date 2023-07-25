
class Sentiment:
    """Includes all the necessary files to run this script"""

    def __init__(self, model='germansentiment'):
        if model == 'germansentiment':
            from germansentiment import SentimentModel
            self.model = SentimentModel()
        else:
            print(f'ERROR: Unknown sentimentmodel {model}')


    def process(self, text):
        if text == '':
            return [[['positive', 0], ['negative', 0], ['neutral', 1]]]
        classes, probabilities = self.model.predict_sentiment([text], output_probabilities = True)
        return probabilities

