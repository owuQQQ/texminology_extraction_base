import os
import re
import glob
import pandas as pd
import numpy as np
from nltk import pos_tag
from nltk import word_tokenize
from KMP_Pattern_matching import KMPSearch

#The first approach is to use the POS to extract terms.
#The pattern is recorded in a txt file in advance.
#Change the directory name when use it

pattern_directory = "C:\\Users\\qiqi1\\Term_resources\\the-acl-rd-tec\\misc"
folder_name = "C:\\Users\\qiqi1\\Term_resources\\_all_annotation_in_sentence"
file_list = glob.glob(os.path.join(os.getcwd(), folder_name, "*.txt"))
Col_names = ['sentence','term']
data = pd.DataFrame(columns = Col_names)

for file in file_list:
    with open(file,"r+") as f:
        for i in range(500):
            text=next(f).strip()
            term=re.findall('[^<term.+][\>$](.*?)</term>',text, re.DOTALL)
            line=re.sub('<[^>]*>', '', text)
            new_sentence=re.sub('\\\/|\\t', ' ', line)
            data.loc[i] = [new_sentence,term]
    f.close()

class pattern_extractor:
    def __init__(self,data,url):
        self.data=data
        self.url=url

    #prerecorded patterns are saved in the ``pattern directory''
    def get_the_prerecord_pattern(self):
        pattern_list=[]
        pattern_file = glob.glob(os.path.join(os.getcwd(), self.url, "*.txt"))
        for file in pattern_file:
            with open(file,'r+') as f:
                patterns=f.readlines()
                for line in patterns:
                    line=line.strip()
                    #new_pattern = re.sub(' ', '+', line)
                    pattern_list.append(line)
        return pattern_list

    #parse the sentence and get the POS tags
    def data_with_tag_sentence(self):
        Tag_lists,Word_lists=[],[]
        for sentence in self.data['sentence']:
            new_sentence=word_tokenize(sentence)
            Res = pos_tag(new_sentence)
            Words, Tags = zip(*Res)
            Tag_lists.append(list(Tags))
            Word_lists.append(list(Words))
        return Tag_lists,Word_lists


    #pattern matching from the longest pattern, term with larger size has the potential to have smaller terms
    #e.g., speech recognition -> speech,  recognition
    #This function return a list of lists, each list correspond to a sentence, the list store the starting index and the size of the term
    #e.g., [5,3] means a pattern is matched at index 5, and it has size of 3 so the word in index 5,6,7 matches a pattern
    def generate_term(self):
        self.data.drop(index=data.index[0],axis=0,inplace=True)
        prediction=[]
        patterns = sorted(self.get_the_prerecord_pattern(), key=lambda x: (-len(x), x))
        Tags,Words=self.data_with_tag_sentence()
        self.data['term']=[i[0].split() for i in self.data['term']]
        self.data['POS']=Tags
        self.data['Words']=Words
        self.data['term_position']=self.data.apply(lambda x:KMPSearch(x.term,x.Words),axis=1)
        for POS_taggs in self.data['POS']:
            for pattern in patterns:
                temp=[]
                new_pattern=pattern.split(" ")
                if KMPSearch(new_pattern,POS_taggs)!=None:
                    temp.append(KMPSearch(new_pattern,POS_taggs))
                    prediction.extend(temp)
        sentence_prediction=[prediction[i:i + len(patterns)] for i in range(0, len(prediction), len(patterns))]
        res=[list(filter(None,i)) for i in sentence_prediction]
        self.data['prediction']=res


ex= pattern_extractor(data,pattern_directory)
ex.generate_term()
print(ex.data)
#TODO test accuracy

# Since the dataset itself has a lot of duplication which each example only has one term labelled
#The accuracy thus should be the accumulation of

#Example:
#he <term id="5506" ann="2">parser</term> scans a user utterance and returns ,
# as output , a list of semantic tuples associated with
# each keyword\/phrase contained in the utterance .

#This example only tagged one term, but in fact it has more than 3.
# The dataset just duplicate the above example and tag the term seperately
#Which makes the calculation of accuracy hard.













