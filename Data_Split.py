#!/usr/bin/env python
# coding: utf-8

# In[1]:


import bs4 as bs
import urllib.request
import re
def get_QaA(scraped_data):
    article = scraped_data.read()

    parsed_article = bs.BeautifulSoup(article,'lxml')

    paragraphs = parsed_article.find_all('p')

    article_text = ""

    for p in paragraphs:
        article_text += p.text

    article_Cluster = re.split('\xa0Q\xa0',article_text)
    
    QaA = []
    for cluster in article_Cluster:
        QaA.append(re.split('[A-Z][A-Z][A-Z]+:',cluster,maxsplit=1))
        
    for response in QaA:   
        if len(response)==1:
            QaA.remove(response)
            
    Question = []
    for Qs in QaA:
        Question.append(re.sub('\xa0','',Qs[0]))
    Question[0]='openning'
    
    Answer = []
    for As in QaA:
        Answer.append(re.sub('\xa0','',As[1]))
    
    return Question,Answer


# In[7]:





# In[8]:





# In[9]:





# In[10]:





# In[ ]:




