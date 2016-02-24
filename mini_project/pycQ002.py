import os, sys, re
path = os.path.dirname(sys.argv[0]) + '\\'
fname = raw_input("File name: ")
try:
    fhand = open(path + fname)
except:
    print "Error!"
    exit()
total = ''
for line in fhand:
    line = line.rstrip()
    x = re.findall('[a-z]', line)
    if len(x) > 0:
        for i in x :
            total += i
print total