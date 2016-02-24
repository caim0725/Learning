import os, sys, string
path = os.path.dirname(sys.argv[0])
fname= raw_input("Enter file name: ")
try:
	fhand = open(path + '\\' + fname)
except:
    print "Wrong file name!"
    exit()
check = dict()
for line in fhand:
    line = line.translate(None, string.punctuation)#delete puctuation
    line = line.lower()
    words = line.split()
    for word in words:
        check[word] = check.get(word, 0) +1#counter for words apeared
incheck = raw_input("Which string you want to find?")
incheck = incheck.lower()
if incheck in check:
    print "The string ",incheck , " do exist and appears for ", check[incheck], " times"
else:
    print "The string ",incheck , " don't exist."
keysort = check.keys()
keysort.sort()#sort the key for right sequence
for key in keysort:
    print key, check[key]