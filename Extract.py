
# coding: utf-8

# In[1]:


from nltk.tag import StanfordNERTagger
from nltk.tag.crf import CRFTagger
from nltk.tokenize import word_tokenize
import warnings
warnings.filterwarnings('ignore')
# warnings.filterwarnings(action='once')
warnings.simplefilter('ignore')
import csv
import time
import subprocess


# In[2]:


import subprocess
def run_command(command):
    p = subprocess.Popen(command,
                     stdout=subprocess.PIPE,
                     stderr=subprocess.STDOUT,shell=True)
    return iter(p.stdout.readline, b'')


# In[3]:


def Info(fname):
	st = StanfordNERTagger('ner-model.ser.gz','stanford-ner.jar', encoding='utf-8')

	run_command('java -cp stanford-ner.jar edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier ner-model.ser.gz -textFile '+fname+' -outputFormat tabbedEntities>Output.tsv')

	time.sleep(5)
	f=open("Output.tsv","r")
	data=csv.reader(f,delimiter='\t')
	row=[]
	for line in data:
		row.append(line)
	f.close()
	return (row)

