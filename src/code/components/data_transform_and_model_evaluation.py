import os
from src.code.logging import LogTool
from src.code.entity import DataTransformationModelEvalConfig
import pandas as pd
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import re
from sklearn.model_selection import train_test_split
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from src.code.utils.common import save_json
from pathlib import Path

class DataTransformationModelEval:
    def __init__(self, config: DataTransformationModelEvalConfig):
        self.config = config


    def transform_and_evaluation(self):

        df=pd.read_csv(f"{self.config.data_path}/complaints_processed.csv")
        df=df[["product","narrative"]]
        df=df[~df['narrative'].isna()]
        MAX_NB_WORDS = 50000
        MAX_SEQUENCE_LENGTH = 250
        EMBEDDING_DIM = 100
        
        def clean_complaint(text):
            """
            text: string
            return: cleaned string
            """
            stop_words = set(stopwords.words('english'))
            text = str(text)
            text = text.lower()
            text = re.compile('[^a-z\s]').sub('', text)
            text = ' '.join(word for word in text.split() if word not in stop_words)
            return text

        tokenizer = Tokenizer(num_words=MAX_NB_WORDS,
                      filters='!"#$%&(\')*+,-./:;<=>?@[\]^_`{|}~',
                      lower=True)
        cleaned_df=df['narrative'].apply(clean_complaint)
        X = tokenizer.texts_to_sequences(df['narrative'].values)
        X = pad_sequences(X, maxlen=MAX_SEQUENCE_LENGTH)
        print('Shape of data tensor:', X.shape)
        y = pd.get_dummies(df['product']).values
        print('Shape of label tensor:', y.shape)
        X_train, X_test, Y_train, Y_test = train_test_split(X,y, test_size = 0.20, random_state = 42)
        print(f"X-test shape : {X_test.shape} ; Y-test shape : {Y_test.shape}")

        model=tf.keras.models.load_model(self.config.model_path)
        accuracy = model.evaluate(X_test,Y_test)
        print('Test set\n  Loss: {:0.3f}\n  Accuracy: {:0.3f}'.format(accuracy[0],accuracy[1]))

        scores={"Loss": accuracy[0],"Accuracy": accuracy[1]}

        
    
    

