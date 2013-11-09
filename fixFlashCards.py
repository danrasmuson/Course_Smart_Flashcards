import re
from tkinter import Tk

def lengthOfTerm(term):
	termLength = term.split()[-1].replace("Word","").lower()
	if termLength == "one":
		return 1
	elif termLength == "two":
		return 2
	elif termLength == "three":
		return 3
	elif termLength == "four":
		return 4
	elif termLength == "five":
		return 5
	return 0

#get clipboard data
r = Tk()
r.withdraw()
result = r.selection_get(selection = "CLIPBOARD")
clipBoard = re.sub(r'[^\x00-\x7F]',"f",result)

#split and format
fullTermList = clipBoard.split("\n\n")
toClipboardStr = ""
for term in fullTermList:
	#remove commas for csv
	if len(term) > 1:
		length = lengthOfTerm(term) #Astronomy - the study of stars
		if length != 0:
			term = term.replace(",","")

			term = term.replace("\n"," ") #remove lines
			term = term.replace("-","") #remove lines joins
			term = term.replace("  "," ") #remove lines joins
			term = term.replace(" ",",",length).replace(","," ",length-1) #puts the comma in
			term = term.replace(", ",",") #remove lines joins
			term = " ".join(term.split()[:-1]) #drop last word (OneWord)

			toClipboardStr += term+"\n"
		else:
			toClipboardStr += term

#put to clipboard
r.clipboard_clear()
r.clipboard_append(toClipboardStr)
r.destroy()
