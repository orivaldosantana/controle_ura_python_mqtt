import re
import numpy as np


class NLPBasico:
  """ Classe com recursos básicos NLP """

  def limpaSenteca(self, inText, porter, stopwords): 
    # deixa passar apenas letras e letras com acentuação 
    text = re.sub('[^a-zA-Záàâãéèêíïóôõöúçñ]', ' ', inText)
    # torna todas as letras minúsculas 
    text = text.lower()
    # divide o texto em palavras gerando um vetor de palavras 
    text = text.split()
    # filtra as palavras vazias e aplica 'porter stemmer' 
    text = [porter.stem(word) for word in text if not word in set(stopwords)]
    text = ' '.join(text)
    return text 

  # código simples para encontrar o melhor elemento de um vetor  
  def encontraMelhor(self, pIn,X):
    bestMetric = 0
    bestI = 0 
    # usar o tamanho a partir do X 
    for i in range(98):
      pData = np.array(X[i])
      metric = np.inner(pIn,pData)
      if metric > bestMetric:
        bestMetric = metric
        bestI = i 
    return [bestMetric,bestI] 
  
  # limiarConf, valor mínimo necessário para considerar que a pergunta é equivalente 
  def encontraComando(self, limiar_conf,sentenca,ps,X, palavras_vazias, dataset, cv):
    # Limpa a sentença / pergunta 
    sent =  self.limpaSenteca(sentenca, ps, palavras_vazias)
    # gera a reprsentação vetorial para a sentença 
    sent_bag = cv.transform([sent]).toarray()
    # encontra a melhor representação na base de dados 
    r = self.encontraMelhor(np.array(sent_bag[0]), X )
    # devolve se contém algum grau de semelhança 
    if (r[0] > limiar_conf ):
      return dataset['PERGUNTAS'][r[1]]
    else: 
      return 'Pergunta desconhecida.' 