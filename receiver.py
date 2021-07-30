"""
############################################################
# Universidad del Valle de Guatemala
# Saúl Contreras
# Juan Fernando de León
# receiver.py
# Laboratorio 2
# Redes
############################################################
"""

import socket
import binascii
from config import *

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return int2bytes(n).decode(encoding, errors)

#Codification
def Codification(bits):
    return str(bits)

#Trasmisión
s = socket.socket()
s.bind(('', port))
s.listen(5)
c, addr = s.accept()
print ("Socket Up and running with a connection from",addr)
while True:
    rcvdData = c.recv(1024)
    if(rcvdData == b''):
        break
    print ("Received message:",Codification(rcvdData))                  #In this line codification is done, python print method converts array into string automatically 
#    sendData = input("N: ")                                            #Print is verification cause it sends the message to the terminal
#    c.send(sendData.encode())
#    if(sendData == "Bye" or sendData == "bye"):
#        break
c.close()
