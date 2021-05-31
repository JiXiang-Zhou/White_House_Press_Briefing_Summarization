#!/usr/bin/env python
# coding: utf-8

# In[1]:


from keybert import KeyBERT
from wordwise import Extractor


# In[5]:


def length_count(sentence):
    a = sentence.split() 
    num = len(a)
    return num


# In[40]:


def press_briefing_extractor_short(doc):
    
    extractor = Extractor()
    keywords = extractor.generate(doc, 5)
    
    model = KeyBERT('distilbert-base-nli-mean-tokens')
    scores=model.extract_keywords(doc, keyphrase_ngram_range=(1, 2))
    
    for key in scores:
        keywords.append(key[0]) 
    
    keywords = list(set(keywords))
    return keywords


# In[27]:


def words_to_sentences(words):
    length = len(words)
    sentence=''
    for i in range(0,length):
        sentence = sentence+' '+words[i]
    return sentence


# In[48]:


def long_paragraph_split(paragraph,length = 400):
    words = paragraph.split()
    words_length = len(words)
    i = 0
    splited_paragraph=[]
    while(i<words_length):
        splited_paragraph.append(words_to_sentences(words[i:i+length]))
        i=i+length
    return splited_paragraph


# In[51]:


def press_briefing_extractor(doc ,length_limit = 400):
    if length_count(doc)<=length_limit:
        keywords = press_briefing_extractor_short(doc)
    else:
        splited_doc = long_paragraph_split(doc, length_limit)
        keywords = []
        for splited_sentence in splited_doc:
            keywords = keywords + press_briefing_extractor_short(splited_sentence)
            keywords = list(set(keywords))
            
    return keywords


# In[ ]:




