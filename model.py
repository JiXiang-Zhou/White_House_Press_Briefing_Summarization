#!/usr/bin/env python
# coding: utf-8

# In[41]:


from Data_Split import *
from KeyWord_Extractor import *
from Search_word_key_word_similarity import *
from summarizer import Summarizer


# In[ ]:


class press_briefing_summarizer(object):
    def __init__(self, link):
        self.link = link
        self.QaAs = []
        self.keywords_list = []
        self.related_Answers = ''
        self.result = ''
        
    def preprocessing(self,length_limit = 400,Q_min = 50, A_min = 22):#parameter don't need to change
        link = self.link
        QaAs = get_QaA(link)
        filtered_QaAs = filterout_short_QaA(QaAs)
        self.QaAs = filtered_QaAs
        
        keywords_list = []
        for QaA in filtered_QaAs:
            keywords = press_briefing_extractor(QaA[0])
            keywords_list.append(keywords)
        
        self.keywords_list = keywords_list
        
    def keyword_search(self,search_word,similarity_value = 0.55):
        related_Answers = ''
        keywords_list = self.keywords_list
        QaAs = self.QaAs
        keywords_list = self.keywords_list
        
        for i in range(len(QaAs)):
            if similarity(search_word,keywords_list[i],similarity_value):
                related_Answers = related_Answers + QaAs[i][1]#add answers in related_Answers
                
        self.related_Answers = related_Answers
        
    def Summary(self,ratio: float = 0.2,
    min_length: int = 40,
    max_length: int = 600,
    use_first: bool = True,
    algorithm: str = 'kmeans',
    num_sentences: int = None,
    return_as_list: bool = False):#parameters from Bert model
        
        model = Summarizer()
        
        text = self.related_Answers
        result = model(text,ratio,min_length,max_length,use_first,algorithm,num_sentences,return_as_list)
        print(result)
        self.result = result
        
    def get_result(self):
        return self.result

