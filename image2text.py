from PIL import Image
from pytesseract import image_to_string
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import tkinter as tk
from tkinter import filedialog, Label, Listbox, Scrollbar, Text, Entry

#-----------------------------------------------------------------------------------------------

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
		chat.configure(state='normal')
		chat.insert('end',string[0][0]+": "+string[0][1]+ '\n')
		chat.configure(state='disabled')

  
#create a tkinter window 
root = tk.Tk()
root.title("AugLi")

# Setting properties & position to the label
label = tk.Label(root,font="Times 14 bold",text = "Image 2 Text Converter")
label.grid(row=0,column=1)

# Create upload & display Buttons
btn1 = tk.Button(root, text='Upload Image', command=UploadAction)
btn2 = tk.Button(root,text="Display Text", command = DisplayText)

btn1.grid(row=1,column=0,pady=4)
btn2.grid(row=1,column=2,pady=4)

# Adding scrollbar & Text widget to display outputs
chatBox = Scrollbar(root)
chat = Text(root, wrap='word', state='disabled', width=50)
chatBox.configure(command=chat.yview)

chat.grid(row=2, columnspan=2, sticky='ewns')
chatBox.grid(row=2, column=2, sticky='ns')

root.mainloop()
