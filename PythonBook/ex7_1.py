import os, sys
path = os.path.dirname(sys.argv[0])
try:
    inpath = raw_input("Enter File Name: ")
    fhand = open(path+'\\'+inpath)
    for line in fhand:
        line = line.rstrip()
        print line.upper()
    fhand.close()
except:
    print "Wrong file name: "+ inpath
