import numpy as np
import pandas as pd

from basico_nlp import NLPBasico 

import nltk
#nltk.download('stopwords')
from nltk.corpus import stopwords
# Escolher um algoritmo mais sofisticado de extração da palavra equivalente (stemmer) 
from nltk.stem.porter import PorterStemmer  


ps = PorterStemmer()

dataset = pd.read_csv('comandos_basicos.csv')
print(  dataset.head(10)  )

palavrasVaziasPT = stopwords.words('portuguese') 

NLPProgramacao = NLPBasico(ps,palavrasVaziasPT) 

NLPProgramacao.criaCorpus(dataset) 

NLPProgramacao.criaBagOfWords()

print( NLPProgramacao.encontraComando(1,"vá em frente") )