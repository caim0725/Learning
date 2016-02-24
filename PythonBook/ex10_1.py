import os, sys
path = os.path.dirname(sys.argv[0]) + '\\'
#find how many from differnd mail
fname = raw_input("File name: ")
try:
    fhand = open(path + fname)
except:
    print "Wrong!"
    exit()
counter = dict()
for line in fhand:
    if not line.startswith("From") : continue
    line = line.split()
    if len(line) <3 :continue
    counter[line[1]]=counter.get(line[1],0) +1
countuple=list()
for key,value in counter.items():
    countuple.append((value,key))
countuple.sort(reverse=True)
print countuple[0][1] , countuple[0][0]

fhand.close()
