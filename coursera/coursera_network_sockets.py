import urllib2
from bs4 import *

fhand = urllib2.urlopen("http://pythonlearn.com")
for line in fhand:
    print line


'''
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('http://www.pythonlearn.com', 80))
mysock.send('GET http://www.pythonlearn.com HTTP/1.0\n\n')
while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    print data
mysock.close()
'''
