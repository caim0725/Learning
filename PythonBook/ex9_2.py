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
countsort = counter.keys()
countsort.sort()
num = 1
for key in countsort:
    print str(num) + "." + key + " : " +str(counter[key]) + " times."
    num += 1
fhand.close()
#check when did the mail sent
dcheck = raw_input("whick mail you want to check? : ")
try:
    f2hand = open(path + fname)
    dcheckdic = dict()
    for line in f2hand:
        if not line.startswith("From") : continue
        line = line.split()
        if len(line) <3 :continue
        if line[1] != countsort[int(dcheck)-1] :continue 
        dcheckdic[line[2]] = dcheckdic.get(line[2],0) +1
except:
    print "Type mistake."
    exit()
dsort = dcheckdic.keys()
dsort.sort()
for key in dsort:
    print key + " : " +str(dcheckdic[key]) + " times."
f2hand.close()
#check how many mail from different domain
