from PIL import Image
from pytesseract import image_to_string
import os
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import tkinter as tk
from tkinter import filedialog
from tkinter import Label, Listbox, Scrollbar
#from tkinter import *


def UploadAction(event=None):
	global filename
	filename = filedialog.askopenfilename()

def DisplayText(event=None):

	#extract string from image
	im = Image.open(filename)
	text = image_to_string(im,lang="eng")
	text_token = word_tokenize(text)

        #remove stop words
	filtered_stop=[]
	stop_words = set(stopwords.words('english'))
	for w in text_token:
		if w.lower() not in stop_words:
			filtered_stop.append(w)
			
	#remove punctuations		 
	punctuation = re.compile(r"[-._@*+'^?!&%$#=—‘,“:;()|0-9]")
	post_punctuation=[]
	for words in filtered_stop:
		word=punctuation.sub("",words)
		if len(word)>0:
			post_punctuation.append(word)
	
        #generate POS tags for each word
	for words in post_punctuation:
		string=nltk.pos_tag([words])
		str1 =(string[0][0],": ",string[0][1])
		#print(str)
		label = Label(root, text = (string[0][0]+": "+string[0][1]))
		#print(nltk.pos_tag([words]))
		label.pack(anchor="center")
		#mylist.insert(END, str1)
		


  
#create a tkinter window 
root = tk.Tk()
root.title("AugLi")
# Open window having dimension 100x100 
root.geometry('1200x1200')  
l1 = tk.Label(root,font="Times 14 bold",text = "Image 2 Text Converter")
#l1.grid(row=1,column=3)
l1.pack(anchor="n")
# Create a Button 
b1 = tk.Button(root, text='Upload Image', command=UploadAction)
b2 = tk.Button(root,text="Display Text", command = DisplayText)

b1.pack(anchor="nw")
b2.pack(anchor="ne")

#scrollbar = Scrollbar(root)
#scrollbar.pack( side = RIGHT, fill = Y )

#mylist = Listbox(root, yscrollcommand = scrollbar.set )
#mylist.pack( side = LEFT, fill = BOTH )
#scrollbar.config( command = mylist.yview )

#b1.grid(row=2,column=2,pady=4)
#b2.grid(row=2,column=4,pady=4)
root.mainloop()
