#Пикуль Мария гр P4109
from collections import Counter

import nltk
import requests

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

from nltk.tokenize import word_tokenize

data = requests.get('https://gist.githubusercontent.com/nzhukov/b66c831ea88b4e5c4a044c952fb3e1ae/raw/7935e52297e2e85933e41d1fd16ed529f1e689f5/A%2520Brief%2520History%2520of%2520the%2520Web.txt')
#print(data.status_code)                                                #Для самопроверки

#print(data.content.strip())                                            #Для самопроверки
data.content.decode('utf-8')
tokens = word_tokenize(data.content.decode('utf-8'))
cnt = Counter([word[1] for word in nltk.pos_tag(tokens)])
tag_counter = dict(cnt)
name_tag_group_map = {
    #Существительное
    "Nouns": ['NN', 'NNP', 'NNPS', 'NNS'],
    #Прилагательное
    "Adjectives": ['JJ', 'JJR', 'JJS'],
    #Глаголы
    "Verbs": ['VB','VBP', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ'],
    #Наречия
    "Adverbs": ["RBR", "RBS"],
    #Междометия
    "Interjections": ['IN'],
    #Предлоги
    "Prepositions": ["PRP", "PRPS"],
}
new_list_words = []
for word in nltk.pos_tag(tokens):
  for tag_name_new, tag_name_old in name_tag_group_map.items():
    if word[1] in set(tag_name_old):
      new_list_words.append(tag_name_new)
cnt = Counter(new_list_words)
tag_counter = dict(cnt)
a = sorted(tag_counter.items(), key=lambda kv: kv[1], reverse=True)
print(a)                                                                #Для самопроверки
file = open('DB.txt', 'w', encoding='utf-8')
file.write(str(a))