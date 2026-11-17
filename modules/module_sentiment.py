import torch
from scipy.special import softmax

class Sentiment:
    """Includes all the necessary files to run this script"""

    def __init__(self, model='germansentiment'):
        if model == 'germansentiment':
            from germansentiment import SentimentModel
            self.model = SentimentModel()
            self.predict_func = self._process_german_sentiment
        elif model == 'multilingual':
            from transformers import AutoModelForSequenceClassification
            from transformers import AutoTokenizer, AutoConfig

            model = f"cardiffnlp/twitter-xlm-roberta-base-sentiment"

            self.tokenizer = AutoTokenizer.from_pretrained(model)
            self.config = AutoConfig.from_pretrained(model)

            # PT
            self.model = AutoModelForSequenceClassification.from_pretrained(model)
            self.model.eval()
            #model.save_pretrained(model)
            self.predict_func = self._process_cardiff_multilingual

        else:
            raise ValueError(f'Unknown sentimentmodel {model}')


    def process(self, text):
        if text == '':
            return [[['positive', 0], ['negative', 0], ['neutral', 1]]]
        ret = [self.predict_func(text)]
        return ret

    # German Sentiment
    def _process_german_sentiment(self, text):
        classes, probabilities = self.model.predict_sentiment([text], output_probabilities = True)
        scores = dict(probabilities[0])
        return [[label, float(scores[label])] for label in ('positive', 'negative', 'neutral')]

    # Cardiff NLP twitter-xlm-roberta-base-sentiment
    def _preprocess_cardiff_multilingual(self, text):
        new_text = []
        for t in text.split(" "):
            t = '@user' if t.startswith('@') and len(t) > 1 else t
            t = 'http' if t.startswith('http') else t
            new_text.append(t)
        return " ".join(new_text)

    def _process_cardiff_multilingual(self, text):
        text = self._preprocess_cardiff_multilingual(text)
        encoded_input = self.tokenizer(text, return_tensors='pt', truncation=True)
        with torch.inference_mode():
            output = self.model(**encoded_input)
        scores = output.logits[0].cpu().numpy()
        scores = softmax(scores)
        scores = {self.config.id2label[i].lower(): float(s) for i, s in enumerate(scores)}
        return [[label, scores[label]] for label in ('positive', 'negative', 'neutral')]


        # Print labels and scores
        #ranking = np.argsort(scores)
        #ranking = ranking[::-1]
        #for i in range(scores.shape[0]):
        #    l = self.config.id2label[ranking[i]]
        #    s = scores[ranking[i]]
        #    print(f"{i+1}) {l} {np.round(float(s), 4)}")

if __name__ == '__main__':
    model_id = 'multilingual'
    model = Sentiment(model=model_id)
    sentiment = model.process("I am happy")
    print(sentiment)
    sentiment = model.process("I am sad")
    print(sentiment)
    sentiment = model.process("I am neutral")
    print(sentiment)
