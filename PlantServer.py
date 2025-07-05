import socket
from datetime import *
from firebase import firebase
import time

firebase = firebase.FirebaseApplication("https://mmp-dbms-default-rtdb.firebaseio.com/",None)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = ''

port = 4444

s.bind((host, port))

s.listen(5)

clientSocket, address = s.accept()

while True:

    # print("Connection established1")
    datarec = clientSocket.recv(1024)
    da = datarec.decode()
    
    print("Connection established"+da+"fire")

    now = datetime.now()

    fireTime = now.strftime(" %d %b, %Y %H:%M:%S")
    date = {
        'info' : "There is a fire in the "+da,
        'time' : fireTime
    }
    if(da == 'home2'):
        result = firebase.post('/fireHistory', date)
        print(result)
