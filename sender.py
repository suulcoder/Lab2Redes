"""
############################################################
# Universidad del Valle de Guatemala
# Saúl Contreras
# Juan Fernando de León
# sender.py
# Laboratorio 2
# Redes
############################################################
"""

import socket
import binascii
import pickle
import numpy
from bitarray import bitarray
from checkSum import findChecksum
from config import *

#noise
def noise(bits):
    my_bits = bitarray() 
    for bit in bits:
        new_bit = int(not(bit)) if numpy.random.choice([0,1], p=[0.95, 0.05]) else bit
        my_bits.append(new_bit)
    return my_bits

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

#Verification
def verification(str_):
    bits = text_to_bits(str_)
    return (bitarray(bits))

#Transmition
s = socket.socket()
s.connect((host,port))
while True:
    str_ = input("Write your message: ")
    my_bitarray = verification(str_)                    #This is verified message
    checkSum = findChecksum(my_bitarray)
    bits = noise(checkSum + my_bitarray)                           #This is message with noise
    s.send(bits)
    if(str == "Bye" or str == "bye"):
        break
#    print ("N:",s.recv(1024).decode())
s.close()