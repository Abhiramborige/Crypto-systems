# Method 1: Using hashlib and hmac modules
import hashlib
import hmac

def make_digest(message, key):
    
    # converting into bytes
    key = bytes(key, 'UTF-8')
    message = bytes(message, 'UTF-8')

    # creating signature from the digest using sha1
    digester = hmac.new(key, message, hashlib.sha1)
    signature1 = digester.hexdigest()
    
    #signature1 = digester.digest()
    print("Hexdigest: ",signature1)

    # other functions to display details
    print ("Digest size is(in bytes): " + str(digester.digest_size)) 
    print ("Block size is(in bytes): " + str(digester.block_size)) 
    print ("Canonical name(encryption Algorithm used): " + digester.name) 
  
# main function
message=input("Enter the message(used in SHA1): ")
key=input("Enter the key(used in MAC): ")   
make_digest(message,key)

print()

# Method 2: Using PyCrypto module
from Crypto.Hash import HMAC,SHA1

def make_digest(message, key):
  key = bytes(key, 'UTF-8')
  message = bytes(message, 'UTF-8')
  h=HMAC.new(key,digestmod=SHA1)
  # to create the digest
  h.update(message)
  # create signature using digest
  print(h.hexdigest()) 

# main function
message=input("Enter the message(used in SHA1): ")
key=input("Enter the key(used in MAC): ")   
make_digest(message,key)

print()

# This is code for SHA-1 Algorithm:
import hashlib
s=input("Enter the message to encrypt: ")
result=hashlib.sha1(s.encode())
print("The output from SHA1: ",result)
print("The hexa decimal output from SHA1: ",result.hexdigest()) 


'''
----------OUTPUT----------
Enter the message(used in SHA1): make the world beautiful
Enter the key(used in MAC): master
Hexdigest:  b5bbb7997bdd387bc38c7a445672ce77b4afd1b4
Digest size is(in bytes): 20
Block size is(in bytes): 64
Canonical name(encryption Algorithm used): hmac-sha1

Enter the message(used in SHA1): make the world beautiful
Enter the key(used in MAC): master
b5bbb7997bdd387bc38c7a445672ce77b4afd1b4

Enter the message to encrypt: Hello all
The output from SHA1:  <sha1 HASH object @ 0x0000017221671570>
The hexa decimal output from SHA1:  08d3934102b1ef2345fbf64e83111dab6b7ddace
'''

'''
Took help from:
1. PyCryptodome documentation
2. Hashlib documentation
Thanks for the help!
'''
