
print ("Both parties agree to a single prime")
prime=int(input("Enter the prime number to be considered: "))

# Primitive root to be used use
print ("Both must agree with single primitive root to use")
root=int(input("Enter the primitive root: "))

# Party1 chooses a secret number
alicesecret=int(input("Enter a secret number for Party1: "))

# Party2 chooses a secret number (bs)
bobsecret=int(input("Enter a secret number for Party2: "))
print("\n")

# Party1 public key A=(root^alicesecret)*mod(prime)

print ("Party1's  public key -> A = root^alicesecre*mod(prime))")
alicepublic=(root**alicesecret)%prime
print ("Party1 public key is: ",alicepublic, "\n")



# Party2 public key B=(root^bobsecret)*mod(prime)
print ("Party2's public key -> B = root^bobsecret*)mod(prime))")
bobpublic=(root**bobsecret)%prime
print ("Party2 public key is", bobpublic, "\n")

# Party1 and Party2 exchange their public keys
# Eve(attacker) nows both parties public keys


# Party1 now calculates the shared key K:
# K = B^(alicesecret)*mod(prime)
print ("Party1 calculates the shared key as K=B^alicesecret*(mod(prime))")
alicekey=(bobpublic**alicesecret)%prime
print ("Party1 calculates the shared key and results: ",alicekey, "\n")

# Party2 calculates the shared key K:
# K = A^(bobsecret)*mod(prime)
print ("Party2 calculates the shared key as K = A^bobsecret*(mod(prime))")
bobkey =(alicepublic**bobsecret)%prime
print ("Party2 calculates the shared key and gets", bobkey, "\n")

#Both Alice and Bob now share a key which Eve cannot calculate
print ("Attacker does not know the shared private key that Party1 & Party2 can now use")

'''
----------OUTPUT----------
Both parties agree to a single prime
Enter the prime number to be considered: 31
Both must agree with single primitive root to use
Enter the primitive root: 11
Enter a secret number for Party1: 98
Enter a secret number for Party2: 60


Party1's  public key -> A = root^alicesecre*mod(prime))
Party1 public key is:  19 

Party2's public key -> B = root^bobsecret*)mod(prime))
Party2 public key is 1 

Party1 calculates the shared key as K=B^alicesecret*(mod(prime))
Party1 calculates the shared key and results:  1 

Party2 calculates the shared key as K = A^bobsecret*(mod(prime))
Party2 calculates the shared key and gets 1 

Attacker does not know the shared private key that Party1 & Party2 can now use
>>> 
'''

'''
Took help from:
1. https://sublimerobots.com/2015/01/simple-diffie-hellman-example-python/
2. https://trinket.io/python/d574095364
3. https://www.wolframalpha.com/widgets/view.jsp?id=ef51422db7db201ebc03c8800f41ba99
Thanks for the help !
'''
