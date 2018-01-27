'''
#Author: Caio Emidio de Andrade Carnelos
#Subject: Download a SimpleList :)
'''
import urllib.request, urllib.parse, urllib.error
import sys

try:
	file = open(sys.argv[1], "r")
except FileNotFoundError:
	f = input("File Name: ")
	file = open(f, "r")

listFiles = file.readlines()

for url in listFiles:
	url = url.strip()
	#strip only to take out '/n'
	name = url.split("/")
	#name take the last name of the link. 
	urllib.request.urlretrieve(url, name[-1])
