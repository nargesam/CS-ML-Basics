'''
Step 0: Download data from:
https://www.kaggle.com/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews

Step 1: EDA (~15 minutes)

Step 2: Data Preprocessing (~20 minutes)
- remove stop words, punctuation, capital letters
- Tokenize
- Stemming
- Lemmatizing

Step 3: Vectorization/Experimentation (~30 minutes)
- n-grams
- embeddings
- one hot encoding
- TFIDF

Step 4: Build Classifiers (~20 minutes)
- LR
- SVM

Step 5: Bonus (any additional time)
- NNs (maybe just a shallow one in keras (~10 minutes))
- BERT

Step 6: Evaluate model (~5 minutes)
- Validate
- Chose model
- Chose metric (classification_report)

Step 7: Submit

Useful libraries:

import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import spacy
import re
import string
import numpy as np

from tqdm import tqdm
tqdm.pandas(desc="progress-bar")

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,classification_report

from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.svm import SVC

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

'''
import pandas as pd
import numpy as np
import nltk
import tensorflow as tf

from nltk.corpus import stopwords
# from nltk.tokenize  import word_tokenize

from sklearn import  model_selection
from tensorflow.keras.preprocessing.text  import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences 


class movieReviewClassifierDnn():
    def __init__(self, datapath):
        self.data = pd.read_csv(datapath)
        self.max_len = 100
        self.vocab_size = 30000
        self.embedding_dim = 300 


    def explain_data(self):
        print(f" You have {len(self.data)} movie reviews.")
        print(f" Here are the columns of the data: {list(self.data.columns)} movien reviews which the labels are distributed as {self.data.sentiment.value_counts()}.")
        print("dataset  is balanced!! ")

        print(type(self.data.sentiment.iloc[0]))


    def tokenizer(self):
        reviews = list(self.data['review'])
        self.data.loc[(self.data.sentiment == 'positive'), 'sentiment'] = 1
        self.data.loc[(self.data.sentiment == 'negative'), 'sentiment'] = 0
        sentiment = list(self.data['sentiment'])

        tokenizer = Tokenizer(num_words=self.vocab_size, oov_token =  '<OOV>')
        tokenizer.fit_on_texts(reviews)
        sequences = tokenizer.texts_to_sequences(reviews)
        self.padded_sequences =  pad_sequences(sequences, maxlen=self.max_len, padding='post')
        
        # self.padded_seq = np.array(pad_sequences)
        self.sentiment = np.array(sentiment)


    def split_train_valid(self):
        self.review_train, self.review_valid, self.sentiment_train,  self.sentiment_valid  =  model_selection.train_test_split(self.padded_sequences, \
                                                                        self.sentiment, test_size=0.2, random_state=42 )
    

    def model(self):
        self.model = tf.keras.Sequential([
            tf.keras.layers.Embedding(self.vocab_size, self.embedding_dim, input_length=self.max_len),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(32, activation='relu'),
            tf.keras.layers.Dense(1, activation='sigmoid')
        ])
        self.model.compile(optimizer='adam', loss='binary_crossentropy',  metrics=['accuracy'])
        print(self.model.summary())


    def train(self):
        callback_lr = tf.keras.callbacks.ReduceLROnPlateau(monitor='val_loss',  factor=0.2,patience=3, min_lr=0.001)
        self.model.fit(x=self.review_train, y=self.sentiment_train, epochs=6,\
             validation_data=(self.review_valid, self.sentiment_valid), callbacks=[callback_lr])

    


if __name__ == "__main__":

    datapath =  'IMDB Dataset.csv'
    # obj = movieReviewClassifierDnn(datapath)
    # obj.explain_data()
    # obj.tokenizer()
    # obj.split_train_valid()
    # obj.model()
    # obj.train()

    obj = movieReviewClassifierNLTK(datapath)
    obj.explain_data()
    obj.preprocessing()


# Layer (type)                 Output Shape              Param #   
# =================================================================
# embedding (Embedding)        (None, 100, 300)          9000000   
# _________________________________________________________________
# flatten (Flatten)            (None, 30000)             0         
# _________________________________________________________________
# dense (Dense)                (None, 32)                960032    
# _________________________________________________________________
# dense_1 (Dense)              (None, 1)                 33        
# =================================================================
# Total params: 9,960,065
# Trainable params: 9,960,065
# Non-trainable params: 0
# _________________________________________________________________
# None
# Train on 40000 samples, validate on 10000 samples
# Epoch 1/10
# 40000/40000 [==============================] - 95s 2ms/sample - loss: 0.3845 - accuracy: 0.8215 - val_loss: 0.3199 - val_accuracy: 0.8607
# Epoch 2/10
# 40000/40000 [==============================] - 95s 2ms/sample - loss: 0.0607 - accuracy: 0.9785 - val_loss: 0.5421 - val_accuracy: 0.8292
# Epoch 3/10
# 40000/40000 [==============================] - 95s 2ms/sample - loss: 0.0127 - accuracy: 0.9959 - val_loss: 0.7311 - val_accuracy: 0.8314
# Epoch 4/10
# 40000/40000 [==============================] - 96s 2ms/sample - loss: 0.0098 - accuracy: 0.9966 - val_loss: 0.8415 - val_accuracy: 0.8280
# Epoch 5/10
# 40000/40000 [==============================] - 96s 2ms/sample - loss: 0.0112 - accuracy: 0.9963 - val_loss: 0.9148 - val_accuracy: 0.8298
# Epoch 6/10
# 40000/40000 [==============================] - 97s 2ms/sample - loss: 0.0105 - accuracy: 0.9967 - val_loss: 0.9363 - val_accuracy: 0.8266
# Epoch 7/10
# 40000/40000 [==============================] - 96s 2ms/sample - loss: 0.0042 - accuracy: 0.9988 - val_loss: 1.0851 - val_accuracy: 0.8192
# Epoch 8/10
# 40000/40000 [==============================] - 97s 2ms/sample - loss: 0.0043 - accuracy: 0.9987 - val_loss: 1.2049 - val_accuracy: 0.8274
# Epoch 9/10
# 40000/40000 [==============================] - 96s 2ms/sample - loss: 0.0077 - accuracy: 0.9976 - val_loss: 1.1466 - val_accuracy: 0.8246
# Epoch 10/10
# 40000/40000 [==============================] - 96s 2ms/sample - loss: 0.0045 - accuracy: 0.9985 - val_loss: 1.1661 - val_accuracy: 0.8290