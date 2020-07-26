import string

main=string.ascii_lowercase

def conversion(plain_text,key):
    index=0
    cipher_text=""

    # convert into lower case
    plain_text=plain_text.lower()
    key=key.lower()
    
    # For generating key, the given keyword is repeated
    # in a circular manner until it matches the length of 
    # the plain text.
    for c in plain_text:
        if c in main:
            # to get the number corresponding to the alphabet
            off=ord(key[index])-ord('a')
            
            # implementing algo logic here
            encrypt_num=(ord(c)-ord('a')+off)%26
            encrypt=chr(encrypt_num+ord('a'))
            
            # adding into cipher text to get the encrypted message
            cipher_text+=encrypt
            
            # for cyclic rotation in generating key from keyword
            index=(index+1)%len(key)
        # to not to change spaces or any other special
        # characters in their positions
        else:
            cipher_text+=c

    print("plain text: ",plain_text)
    print("cipher text: ",cipher_text)

plain_text=input("Enter the message: ")
key=input("Enter the key: ")

# calling function
conversion(plain_text,key)
