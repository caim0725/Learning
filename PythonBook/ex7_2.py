import os, sys
path = os.path.dirname(sys.argv[0])
try:
    inpath = raw_input("Enter File Name: ")
    fhand = open(path+'\\'+inpath)
    sum = 0.0
    count = 0
    for line in fhand:
        if line.startswith("X-DSPAM-Confidence:") :
            sum += float(line.lstrip('X-DSPAM-Confidence: ').rstrip())
            count += 1
    print "Average spam confidence: " , sum/count
except:
    print "GG"
