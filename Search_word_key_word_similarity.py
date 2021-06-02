#!/usr/bin/env python
# coding: utf-8

# In[1]:


import spacy


# In[167]:


def similarity(search_word, keyword_list,similarity_value = 0.55 ):
    nlp = spacy.load('en_core_web_md')
    search_word_tokens = nlp(search_word)
    similarity = False
    
    for keyword in keyword_list:
        
        if similarity:
                break
        keyword_tokens = nlp(keyword)
        
        for keyword_token in keyword_tokens:
            
            if similarity:
                break
            
            for search_word_token in search_word_tokens:
                similarity_val = keyword_token.similarity(search_word_token)
                if similarity_val >= similarity_value:
                    similarity = True
                    break
            
    return similarity

