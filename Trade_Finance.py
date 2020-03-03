#!/usr/bin/env python
# coding: utf-8

# #                                                                   Business Case

# In[1]:


from PIL import Image
import pandas as pd
import glob
#Image.open('Business Case.png')


# ### READING THE FILE PATH

# In[2]:


path_pdf1 = 'data/*.pdf'  
files_pdf1 = glob.glob(path_pdf1)
files_pdf1


# ### IMPORT OCR MODULE

# In[3]:


import OCR
#PDFTOPPMPATH = r"./poppler/bin/pdftoppm.exe"


# In[4]:


k=1
dpi=300
documentText, fname=OCR.Convert(files_pdf1[k], dpi,str(k))


# In[5]:


print (documentText[0])


# # ----XX----

# 
# 
# 
# 
# ### IMPORT INFORMATION EXTRACTION ( NLP) MODULE

# In[6]:


import Extract
df=pd.DataFrame(Extract.Info(fname))


# In[7]:


import Align


# In[10]:


df_final=Align.Info(df)


# ### PRINT FINAL OUTPUT

# In[19]:


df_final=df_final[0:1]
print(df_final)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




