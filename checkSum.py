"""
############################################################
# Universidad del Valle de Guatemala
# Saúl Contreras
# Juan Fernando de León
# checkSum.py
# Laboratorio 2
# Redes
############################################################
"""

# Function to find the Checksum of Sent Message
from bitarray import bitarray
import sys

def findChecksum(sent_message):
    
    # Dividing sent message in packets of k bits.
    my_bytes = []
    i = 0
    while i < len(sent_message):
        my_bytes.append(bitarray(sent_message[i:i+8]))
        i += 8

    # Calculating the binary sum of packets
    # sum = bitarray('00000000')
    sum = int("00000000", 2)
    for byte in my_bytes:
        sum += int(byte.to01(), 2)

    sum = bin(sum)[2:]

    # Adding the overflow bits
    if(len(sum) > 8):
        x = len(sum) - 8
        sum = bin(int(sum[0:x], 2) + int(sum[x:], 2))[2:]
    if(len(sum) < 8):
        sum = '0'*(8-len(sum))+sum

    # Calculating the complement of sum
    check_sum = bitarray()
    for i in sum:
        if(i == '1'):
            check_sum.append(0)
        else:
            check_sum.append(1)

    return check_sum
  
# Function to find the Complement of binary addition of
# k bit packets of the Received Message + Checksum
def checkReceiverChecksum(received_message):

    my_bytes = []
    for bite in received_message:
        my_bytes.append(bitarray(f'{bite:0>8b}'))

    # CheckSum
    check_sum = my_bytes[0]

    # Actual Msg
    received_message = my_bytes[1:]

    # Calculating the binary sum of packets + checksum
    receiver_sum = int(check_sum.to01(), 2)
    msg = bitarray()
    for byte in received_message:
        receiver_sum += int(byte.to01(), 2)
        msg += byte

    receiver_sum = bin(receiver_sum)[2:]

    # Adding the overflow bits
    if(len(receiver_sum) > 8):
        x = len(receiver_sum) - 8
        receiver_sum = bin(int(receiver_sum[0:x], 2)+int(receiver_sum[x:], 2))[2:]

    # Calculating the complement of sum
    receiver_check_sum = ''
    for i in receiver_sum:
        if(i == '1'):
            receiver_check_sum += '0'
        else:
            receiver_check_sum += '1'

    return (receiver_sum, msg)

def validateCheckSum(receiver_check_sum):
    '''Validate if Received checkSum is correct'''
    # # If sum = 0, No error is detected

    print("\n-----------------------------------------------")
    print("\t\tError Detection")

    if(receiver_check_sum == '11111111'):
        print("\nReceiver Checksum is equal to 1. Therefore,")
        print("STATUS: ACCEPTED")
        return True
    # Otherwise, Error is detected
    else:
        print("\nReceiver Checksum is not equal to 1. Therefore,")
        print("STATUS: ERROR DETECTED")
    
    return False