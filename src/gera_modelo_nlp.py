import numpy as np
import pandas as pd

from basico_nlp import NLPBasico 

import nltk
nltk.download('stopwords')
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

""" Várias linhas para testes  
ande para frente
vá para frente
siga em frente
um passo a frente
frente
ande para trás
vá para trás
um passo para trás
trás
vire para esquerda
esquerda
vire para direita
direita
"""

print( NLPProgramacao.encontraComando(1,"frente por 400 milisegundos") )


import pickle

pickle.dump(NLPProgramacao, open("NLPProgramacao.pickle", "wb"))

