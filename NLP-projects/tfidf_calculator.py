"""
claculate TF_IDF for every term in collection of documents

write  a class that calculates the TFIDF for very term and returns TFIDF vector 
TODO: 
1- calculate TF for each term in each document DONE
2-calculate IDF for each term in each document DONE
3- returns TF*IDF DONE
3- for each term calculate vector DONE 
"""

import sklearn

import glob
import math
import os
import re


class claculateTFIDFForTerm():
    def __init__(self, filepath):
        
        self._read_files(filepath)
        
        # No of documents
        self.N = len(self.corpus)
    
    def _read_files(self, filepath):

        file_list = glob.glob(os.path.join(os.getcwd(), "data", "*.txt"))
        self.corpus = []

        for file_path in file_list:
            with open(file_path, encoding='iso-8859-1') as f_input:
                self.corpus.append(f_input.read())


    def TF(self, term, doc_idx):
        doc = self.corpus[doc_idx]
        doc = doc.strip().lower()
        doc = re.split('\W+', doc)

        if term not in doc: 
            return float('-inf')
        
        term_cnt = doc.count(term)
        doc_term = len(doc)
        return term_cnt / doc_term
    
    def IDF(self, term):
        num_doc_with_term = 0
        for doc in self.corpus:
            if term in doc:
                num_doc_with_term += 1
        
        return math.log(self.N / num_doc_with_term)


    def TFIDFVectorizer(self, term):
        idf_term = self.IDF(term)

        self.vector = [0]*(self.N)

        for i in range(len(self.vector)):
            tf = self.TF(term, i)
            if tf == float('-inf'):
                tf = 0
            self.vector[i] = tf*idf_term
        
        return self.vector




if __name__ == "__main__":
    filepath = './data/'

    obj = claculateTFIDFForTerm(filepath)
    
    v = obj.TFIDFVectorizer('is')
    print(v)
    print(len(v))
    # print(obj.TF('is', 0))
    # print(obj.IDF('is'))



        