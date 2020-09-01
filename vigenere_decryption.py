import string

main=string.ascii_lowercase
def conversion(cipher_text,key):
    index=0
    plain_text=""

    # convert into lower case
    cipher_text=cipher_text.lower()
    key=key.lower()
    
    for c in cipher_text:
        if c in main:
            # to get the number corresponding to the alphabet
            off=ord(key[index])-ord('a')

            positive_off=26-off
            decrypt=chr((ord(c)-ord('a')+positive_off)%26+ord('a'))
            
            # adding into plain text to get the decrypted messag
            plain_text+=decrypt
            
            # for cyclic rotation in generating key from keyword
            index=(index+1)%len(key)
        else:
            plain_text+=c

    print("cipher text: ",cipher_text)
    print("plain text (message): ",plain_text)

cipher_text=input("Enter the message to be decrypted: ")
key=input("Enter the key for decryption: ")

# calling function
conversion(cipher_text,key)

'''
----------OUTPUT----------
Enter the message to be decrypted: he xzsdi zu brxh io etvuvni
Enter the key for decryption: awesome world
cipher text:  he xzsdi zu brxh io etvuvni
plain text (message):  hi there my name is abhiram
>>>
'''

'''
Took help from:
1. https://www.youtube.com/watch?v=FAbkLSktxWQ
2. https://www.youtube.com/watch?v=zLbZM_MA3qE&t=575s
'''

