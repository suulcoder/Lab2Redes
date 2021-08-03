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

from enum import Flag
from hamming import calcRedundantBits, detectError
from checkSum import checkReceiverChecksum, validateCheckSum
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
    rcvdData, address = c.recvfrom(1024)
    if(rcvdData == b''):
        break

    rcvd_check_sum, received_msg = checkReceiverChecksum(rcvdData)

    validCheckSum = validateCheckSum(rcvd_check_sum)

    if (not validCheckSum):
        '''If the check sum is not valid les correct the error'''
        isInvalid = True
        print("\n\t\tError Correction")
        while isInvalid:
            r = calcRedundantBits(len(received_msg))
            print("\nredundant bits", r)
            print("Error Data is " + received_msg.to01())
            correction = detectError(received_msg, r)
            print("The position of error is " + str(correction))
            isInvalid = False

    print ("\nRECEIVED MSG:",Codification(received_msg.tobytes()))                  #In this line codification is done, python print method converts array into string automatically 
#    sendData = input("N: ")                                            #Print is verification cause it sends the message to the terminal
#    c.send(sendData.encode())
#    if(sendData == "Bye" or sendData == "bye"):
#        break
c.close()
