import socket
path = raw_input("URL: ")
try:
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    mysock.connect((path.split('/')[2], 80))
    
    mysock.send('GET '+path+' HTTP/1.0\n\n')
   
except:
    print "Valid URL!"
    exit()
count = 0
while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    count = count + len(data)
    if count < 3000:
        print data
print count
    
mysock.close()