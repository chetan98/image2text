# Image2Text

The target of this project is to Extract Text from Images and then provide the Part of Speech (POS Tags) for each word of the extracted text.

### What is POS tagging ?

It is a process of converting a sentence to forms – list of words, list of tuples (where each tuple is having a form (word, tag)). 
The tag in case of is a part-of-speech tag, and signifies whether the word is a noun, adjective, verb, and so on.

![alt text](https://media.geeksforgeeks.org/wp-content/uploads/pos-1.jpg)

## Getting Started

These instructions will help you to Upload Image to  Display the extracted the POS tags from the Image .

## Prerequisites

**pip 3** - PIP is a standard package-management system used to install and manage software packages written in Python.

The executable file for the pip tool is called pip on Windows and pip3 on OS X and Linux.
While pip comes automatically installed with Python 3.4 on Windows and OS X, you must install it separately on Linux. 
To install pip3 on Ubuntu or Debian Linux, open a new Terminal window and enter ``` sudo apt-get install python3-pip ```

## Libraries Required

**pillow** - Pillow is a Python Imaging Library (PIL), which adds support for opening, manipulating, and saving images.

**pytesserect** - Python-tesseract is an optical character recognition (OCR) tool for python. 
That is, it will recognize and “read” the text embedded in images.

``` pip 3 install pillow pytesseract ```

**nltk** - The Natural Language Toolkit (NLTK) is a platform used for building Python programs that work with human language data for text processing, tokenization, parsing, classification, stemming, tagging and semantic reasoning.

``` sudo apt install python3-nltk```

**tkinter** - The Tk toolkit helps to create GUI for the python program.

```sudo apt-get install python3-tk```

## Text Extraction

**_extract string from image_**

```	
im = Image.open(filename)
text = image_to_string(im,lang="eng")
text_token = word_tokenize(text) 
  ```
  
 ## Remove Stopwords & Punctuations

**_Stopwords_** : Stopwords are the words which does not add much meaning to a sentence. They can safely be ignored without sacrificing the meaning of the sentence. For example, the words like the, he, have etc.

**To check the list of stopwords you can type the following commands in the python shell.**
```
import nltk
from nltk.corpus import stopwords
set(stopwords.words('english'))
```
**_Punctuations_** : The marks, such as full stop, comma, question mark and brackets, are not required and should be removed.

## GUI Designing

The tkinter toolkit uses various _widgets_ to help create a GUI.
To undestand the working of the widgets [visit](https://www.tutorialspoint.com/python/python_gui_programming.htm) 

## Author 

- Chetan Rawat [chetan98](https://github.com/chetan98)
