import re
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer 

class NLPBasico:
  """ Classe com recursos básicos NLP """

  def __init__(self, _porter, _palavrasVazias ):
    self.porter = _porter 
    self.palavrasVazias = _palavrasVazias 
    self.corpus = [] 
    self.X = [] 
    self.Y = [] 
    self.cv = -1  

  def limpaSenteca(self, inText): 
    # deixa passar apenas letras e letras com acentuação 
    text = re.sub('[^a-zA-Záàâãéèêíïóôõöúçñ]', ' ', inText)
    # torna todas as letras minúsculas 
    text = text.lower()
    # divide o texto em palavras gerando um vetor de palavras 
    text = text.split()
    # filtra as palavras vazias e aplica 'porter stemmer' 
    text = [self.porter.stem(word) for word in text if not word in set(self.palavrasVazias)]
    text = ' '.join(text)
    return text 

  # código simples para encontrar o melhor elemento de um vetor  
  def encontraMelhor(self, pIn):
    melhorMetrica = 0
    melhorI = 0 
    proporcaoMelhorCasamento = 0 
    maximoCasamento = np.inner(pIn,pIn)
    # usar o tamanho a partir do X 
    for i in range(len(self.X)):
      pData = np.array(self.X[i])
      metrica = np.inner(pIn,pData)
      if metrica > melhorMetrica:
        melhorMetrica = metrica
        melhorI = i 
        proporcaoMelhorCasamento = metrica / maximoCasamento 
    return [melhorMetrica,melhorI,proporcaoMelhorCasamento]  
  
  # limiarConf, valor mínimo necessário para considerar que a pergunta é equivalente 
  def encontraComando(self, limiar_conf, sentenca):
    # Limpa a sentença / pergunta 
    sent =  self.limpaSenteca(sentenca)
    # gera a reprsentação vetorial para a sentença 
    sentBoW = self.cv.transform([sent]).toarray()
    # encontra a melhor representação na base de dados 
    r = self.encontraMelhor(np.array(sentBoW[0]))
    # devolve se contém algum grau de semelhança 
    if (r[0] >= limiar_conf ):
      print("Casamento: ",r[2]*100,"%") 
      return self.Y[r[1]]
    else: 
      return -1  

  # Bag of Words 
  def criaBagOfWords(self, _features = 15):
    self.cv = CountVectorizer( max_features = _features )
    self.X = self.cv.fit_transform(self.corpus).toarray() 
    print("BoW:\n", self.X) 
    print("Características:", self.cv.get_feature_names_out() )

  # Extrai e organiza todos os comandos NLP em vetor 
  def criaCorpus(self, _dataSet):
    self.Y = _dataSet.iloc[:,1].values  
    print(self.Y) 
    for i in range(0,len(_dataSet['comando nlp'])): 
      texto = self.limpaSenteca( _dataSet['comando nlp'][i])
      self.corpus.append(texto)
    print(self.corpus) 

  