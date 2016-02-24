import urllib
path = raw_input("URL: ")
try:
    fhand = urllib.urlopen(path)
except:
    print "Valid URL!"
    exit()
count = 0
for line in fhand:
    count += len(line)
    line = line.strip()
    if count < 3000 : print line
    
print count