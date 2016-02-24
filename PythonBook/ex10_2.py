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
    counter[line[5].split(":")[0]]=counter.get(line[5].split(":")[0],0) +1
countuple=list()
for key,value in counter.items():
    countuple.append((key,value))
countuple.sort()
for key,value in countuple:
    print key , value

fhand.close()
