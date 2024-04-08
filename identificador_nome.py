import csv
import pandas as pd
import nltk

def identifica_nome():
  with open('/home/ermeson/Documents/Unifor/Mat. Discreta/dados/ibge-fem-10000.csv', 'r') as file:
    names_fem = pd.DataFrame([data[0] for data in csv.reader(file)][1:], columns=['name'])
    names_fem['gender'] = 'feminino'

  with open('/home/ermeson/Documents/Unifor/Mat. Discreta/dados/ibge-mas-10000.csv', 'r') as file:
    names_mas = pd.DataFrame([data[0] for data in csv.reader(file)][1:], columns=['name'])
    names_mas['gender'] = 'masculino'
  
  names = pd.concat([names_mas, names_fem])
  names = names.sample(frac=1).reset_index(drop=True)

  len_teste = int(0.1 * len(names))  # 10% dos dados para teste
  names_teste = names.iloc[:len_teste]
  names_treinamento = names.iloc[len_teste:]

  names_treinamento['features'] = names_treinamento['name'].apply(lambda name: {'last_letter': name[-1]})
  names_teste['features'] = names_teste['name'].apply(lambda name: {'last_letter': name[-1]})

  classifier = nltk.NaiveBayesClassifier.train(zip(names_treinamento['features'], names_treinamento['gender']))

  acuracia = nltk.classify.accuracy(classifier, zip(names_teste['features'], names_teste['gender']))
  print("Acurácia do classificador:", acuracia)

  nome_teste = 'MARYA'
  gender = classifier.classify({'last_letter':nome_teste[-1]})
  print(gender)

identifica_nome()
