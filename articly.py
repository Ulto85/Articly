from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
import requests
from bs4 import BeautifulSoup
import ssl
from newspaper import Article
from nltk import sent_tokenize
class Articly:
    def __init__(self):
        pass
    def specify(self,user_input,url,amount_of_sentences = 2):
        article = Article(url)
        article.download()
        article.parse()
        article.parse()
        article.nlp()
        text = article.text
        sent_list = sent_tokenize(text)

        def responder(use_input):
            sent_list.append(use_input)
            vectors = CountVectorizer().fit_transform(sent_list)
            sims = cosine_similarity(vectors[-1], vectors)
            sims_list = sims.flatten()
            second_list = sims_list[:-1]
            respond = ''
            response = 0
            sent_count = 0

            for i in range(len(sims_list)):
                if sent_count > amount_of_sentences:
                    break
                if i != len(sims_list - 1):
                    if sims_list[i] > 0.0:
                        respond += sent_list[i]
                        response += 1
                        sent_count += 1
            if response == 0:
                print("NA")
            else:
                print(respond)
            sent_list.remove(use_input)

        responder(user_input)




articly = Articly()
