'''
Sentiment analysis

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
import sklearn

import pandas as pd

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer 
from sklearn import feature_extraction, ensemble, model_selection
from sklearn.svm import SVC
from sklearn import metrics


class MovieReviewClassifier():
    def __init__(self, file_path):
        self.data = pd.read_csv(file_path, header=0)
        self.data = self.data.sample(1000)


    def EDA(self):
        print("\n\n")
        print("**-"*20)
        print("**-"*20)

        print(f"**- there are {self.data.shape[0]} reviews in this dataset \n")
        print(f"**- there are {self.data.shape[1]} fiels in this dataset \n")
        print(f"**- these are the column names: {self.data.columns} \n ")
        print(f"**- there are {len(self.data['sentiment'].unique())} unique labels for sentiment \n")
        print(f"**- Here is the lable frequency: {self.data['sentiment'].value_counts()} \n ")

        print("**- some of the data looks like this: ")
        print(self.data.head(5))

        print("**-"*20)
        print("**-"*20)
        print("\n\n")



    def _process_text(self, text):
            stop_words = stopwords.words('english')
            lemmatizer = WordNetLemmatizer()
            tmp = [w for w in word_tokenize(text) if w not in stop_words]
            return ' '.join([lemmatizer.lemmatize(w) for w in tmp])


    def preprocess(self):

        self.data['sentiment'] = self.data['sentiment'].map({'positive':1, 'negative':0})
        
        # change test to lower
        self.data['review'] = self.data['review'].str.lower()
        
        # tokenize + stop words removal + lemmatizer 
        self.data['processed'] = self.data.review.apply(self._process_text)


    def vectorize(self):
        tfidf_vectorizer = feature_extraction.text.TfidfVectorizer()
        self.X = tfidf_vectorizer.fit_transform(self.data['processed'])
    

    def _train_test_split(self):
        X_train, X_test, Y_train, Y_test = model_selection.train_test_split(\
                                            self.X, \
                                            self.data.sentiment, \
                                            test_size=0.3)
        
        return X_train, X_test, Y_train, Y_test
    
    
    def train_RandormForest(self):
        
        X_train, X_test, Y_train, Y_test = self._train_test_split()

        model = sklearn.ensemble.RandomForestClassifier(max_depth=100, random_state=0)
        model.fit(X_train, Y_train)

        # evaluate
        Y_pred = model.predict(X_test)
        acc = model.score(X_test, Y_test)
        acc_score = metrics.accuracy_score(Y_test, Y_pred)

        confusuin_matrix = sklearn.metrics.confusion_matrix(Y_test, Y_pred)
        
        print("**-"*20)
        print("**-"*20)
        print("\n\n")
        
        print(f" The acc score for the model is  {acc} \n")
        print(f" The acc score for the model is  {acc_score} \n")

        print(f"\n the confusion matrix = \n {confusuin_matrix} \n ")

        print("**-"*20)
        print("**-"*20)
        print("\n\n")



    def train_SVM(self):
        X_train, X_test, Y_train, Y_test = self._train_test_split()

        model = sklearn.svm.SVC() 
        model.fit(X_train, Y_train)

        # evaluate
        Y_pred = model.predict(X_test)
        acc = model.score(X_test, Y_test)
        confusuin_matrix = sklearn.metrics.confusion_matrix(Y_test, Y_pred)
        
        print("**-"*20)
        print("**-"*20)
        print("\n\n")
        
        print(f" The acc score for the model is  {acc} \n")
        print(f"\n the confusion matrix = \n {confusuin_matrix} \n ")

        print("**-"*20)
        print("**-"*20)
        print("\n\n")


    

if __name__ == "__main__":
    file_path = '/Users/ns5kn/Documents/insight/cs-practical/IMDB_Dataset.csv'

    classifier = MovieReviewClassifier(file_path)

    classifier.EDA()
    classifier.preprocess()
    classifier.vectorize()
    classifier.train_RandormForest()
    classifier.train_SVM()
