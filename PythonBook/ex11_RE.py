import os, sys, re
path = os.path.dirname(sys.argv[0]) + '\\'
#find how many from differnd mail
fname = raw_input("File name: ")
try:
    fhand = open(path + fname)
except:
    print "Wrong!"
    exit()

for line in fhand:
    line = line.rstrip()
    x = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-zA-Z0-9]', line)
    if len(x) > 0 :
        print x
fhand.close()
