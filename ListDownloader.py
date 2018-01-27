'''
#Author: Caio Emidio de Andrade Carnelos
#Subject: Download a SimpleList :)
'''

import urllib.request, urllib.parse, urllib.error
import sys
from tkinter import filedialog
from tkinter import *

try:
	file = open(sys.argv[1], "r")
except FileNotFoundError:
	#If FileNotFoundError, Open a window with Tkinter only to find in GUI mode :)
	root = Tk()
	root.filename =  filedialog.askopenfilename(title = "Select file",filetypes = (("Text Files","*.txt"),("all files","*.*")))
	file = open(root.filename, "r")

listFiles = file.readlines()

for url in listFiles:
	url = url.strip()
	#strip only to take out '/n'
	name = url.split("/")
	#name take the last name of the link. 
	urllib.request.urlretrieve(url, name[-1])
