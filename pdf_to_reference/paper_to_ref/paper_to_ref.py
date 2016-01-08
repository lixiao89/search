import pdf2txt
import operator
import re

k = '-o'
v = "out.txt"
fname = "2.pdf"
pdf2txt.main(fname, k, v)

ftxt = open("out.txt","r")

with open("ref.txt","wb") as f:
    
    for line in ftxt:
        if re.search('^\[\d+\]\s\D', line):
            ref = (line + " " + next(ftxt) + next(ftxt)).rstrip('\n')
            f.write(ref + "\n")
            
