#Chatty_v1
#san-s1819
#I did not follow proper coding standards.Just getting into the world of github.

#tkinter is used for designing GUI's
import tkinter as tk
from tkinter import *
from tkinter.scrolledtext import *

import io
import random #randmozing stuff
import string # to process standard python strings
import warnings #to ignore deprecation warning
import numpy as np

#Popular ML library
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
warnings.filterwarnings('ignore')

#A basic library used for Natural Language Processing(NLP)
import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('popular', quiet=True) # for downloading packages

#Function used for greeting a user
def greeting(sentence):
    """If user's input is a greeting, return a greeting response"""
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


# Generating response
def response(user_response):
    robo_response=''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    #converts raw documents to a matrix of tfidf vectors
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    #Cosine_similarity :: two documents are converted into vectors. Angle between the vectors
    #is found out and the angle tells us about the similarity between them
    idx=vals.argsort()[0][-2]
    #Multidimensional array to a vector
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        robo_response=robo_response+"I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response+sent_tokens[idx]
        return robo_response
    
def printop():
   
    cur=""
    user_response = E1.get()
    Tb.insert(END,"USER:"+user_response+"\n")
    user_response=user_response.lower()
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' ):
            
            cur=""+"ROBO: You are welcome.."
        else:
            if(greeting(user_response)!=None):
                cur=""+"ROBO: "+greeting(user_response)
            else:
                cur=""+"ROBO: "+response(user_response)
                sent_tokens.remove(user_response)
    else:
        
        cur=""+"ROBO: Bye! take care.."
    
    cur+="\n"
    Tb.insert(END,cur)





#Reading in the corpus
with open('context.txt','r', encoding='utf8', errors ='ignore') as fin:
    raw = fin.read().lower()

#TOkenisation
sent_tokens = nltk.sent_tokenize(raw)# converts to list of sentences
word_tokens = nltk.word_tokenize(raw)# converts to list of words

# Preprocessing
lemmer = WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))
#Translate is used for assigning none vlaue for each puntuation present,thus removing puntuations 

# Keyword Matching
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]

#GUI Part
top = tk.Tk()
top.title("Chatty")

can = tk.Canvas(top, width=80, height=60) 

l = Label( text="Please enter :")
l.grid(row=0,column=0)

E1 = Entry(top, bd =5,width=80)
E1.grid(row=0,column=1)

Tb = ScrolledText(top, height='20', width='80', wrap=WORD)
Tb.grid(row=1,columnspan=3)

w=tk.Button(top,text="Get Response!",command=printop,activebackground="blue",activeforeground="red")
w.grid(row=0,column=2)

can.grid()
top.mainloop()       
    


