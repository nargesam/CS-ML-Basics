import re  
import string
import nltk
import spacy
import pandas as pd
import numpy as np 
import  math


from spacy.matcher import Matcher 
from spacy.tokens import Span 
from spacy import displacy 
import en_core_web_sm


pd.set_option('display.max_colwidth', 200)

# loading Hearst pattern 
nlp = spacy.load("en_core_web_sm")

text = "GDP in developing countries such as Vietnam will continue growing \
        at a high rate." 

# spacy obj
doc = nlp(text)
displacy.render(doc, style='dep')


# for  token in doc: 
#     print(f" {token.text} --> {token.dep_} --> {token.pos_}")


# pattern: X such as Y
pattern = [ {'DEP': 'admod', 'OP':'?'},
            {'POS': 'NOUN'},
            {'LOWER': 'such'},
            {'LOWER': 'as'},
            {'DEP': 'admod', 'OP':'?'},
            {'POS': 'PROPN'}
            ]

matcher = Matcher(nlp.vocab)

matcher.add("Matching_1", None, pattern)
matches = matcher(doc)

span = doc[matches[0][1]: matches[0][2]]
print(span)



