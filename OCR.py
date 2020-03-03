
# coding: utf-8

# In[4]:


from PIL import Image
import pytesseract
from pdf2image import convert_from_path
import glob


# In[5]:
#pytesseract.pytesseract.tesseract_cmd = r'C:\Users\khimanshu\Desktop\Tesseract-OCR\tesseract'
#PDFTOPPMPATH = r"./poppler/bin/pdftoppm.exe"
#PDFTOPPMPATH = r"./poppler/bin"

def Convert(files_pdf, dpi, k):
	pages = convert_from_path(files_pdf, dpi)
	text_out=[]
	for j in range(0,len(pages)):
		pages[j].save('out'+str(j)+'.png')
		text_out.append(pytesseract.image_to_string(Image.open('out'+str(j)+'.png')))
	f=open("TF"+k+".txt",'wb')
	for item in text_out:
		f.write(item.encode('utf8'))
	f.close()
	fname = "TF"+k+".txt"
	#document=''
	numLines = 0
	with open(fname,'rb') as f:
		for line in f:
			line=line.decode('utf8')
			numLines += 1
	chunkSize = 1000
	numChunks = numLines//chunkSize
	documentText=[]
	with open(fname,'rb') as f:
		for i in range(numChunks+1):
			document = ''
			for j in range(chunkSize):
				document+=str(f.readline().decode('utf8'))
			documentText.append(document)
	return (documentText,fname)
