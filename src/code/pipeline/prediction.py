import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
import re
from nltk.corpus import stopwords

import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import os


class PredictionPipeline:
    def __init__(self):
        self.model = tf.keras.models.load_model(os.path.join("artifacts","model","model.tf"))

    def transform_and_predict(self, text):
        stop_words = set(stopwords.words('english'))
        def clean_complaint(text):
            """
                text: string
                return: cleaned string
            """
            text = str(text)
            text = text.lower()
            text = re.compile('[^a-z\s]').sub('', text)
            text = ' '.join(word for word in text.split() if word not in stop_words)
            return text
        cleaned_text=clean_complaint(text)
        #max number of words to be used. (most frequent)
        MAX_NB_WORDS = 50000
        # Max number of words in each complaint.
        MAX_SEQUENCE_LENGTH = 250
        EMBEDDING_DIM = 100
        
        tokenizer = Tokenizer(num_words=MAX_NB_WORDS,
                            filters='!"#$%&(\')*+,-./:;<=>?@[\]^_`{|}~',
                            lower=True)
        new_complaint=[cleaned_text]
        seq = tokenizer.texts_to_sequences(new_complaint)
        padded = pad_sequences(seq, maxlen=MAX_SEQUENCE_LENGTH)
        pred = self.model.predict(padded)
        labels = ['credit_card',
        'credit_reporting',
        'debt_collection',
        'mortgages_and_loans',
        'retail_banking']
        return pred, labels[np.argmax(pred)]

        

