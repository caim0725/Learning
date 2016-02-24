import os, shutil,sys
print sys.argv[0]
print os.path.dirname(sys.argv[0])
path = os.path.dirname(sys.argv[0])
fhand = open(path+'/mbox-short.txt')
print fhand
fhand.close()