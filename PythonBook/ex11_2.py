import os, sys, re
path = os.path.dirname(sys.argv[0]) + '\\'
#find how many from differnd mail
fname = raw_input("File name: ")
try:
    fhand = open(path + fname)
except:
    print "Wrong!"
    exit()
sum=0
count = 0
for line in fhand:
    line = line.rstrip()
    x = re.findall('^New .*: ([0-9]+)', line)
    if len(x)>0:
        sum += float(x[0])
        count += 1
print sum / count
fhand.close()
