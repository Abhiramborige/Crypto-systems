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

            decrypt_num=ord(c)-ord('a')-off
            # sometimes decrypt_num may go negative
            if decrypt_num<0:
                decrypt_num+=26
                
            # default condition
            decrypt=chr(decrypt_num+ord('a'))
            
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
