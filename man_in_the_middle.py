# the public parameters are passed as they are known globally 
def attacker(prime, root, alicepublic, bobpublic):
    attacksecret1=int(input("Enter a secret number1 for attacker: "))
    attacksecret2=int(input("Enter a secret number2 for attacker: "))
    print('\n')
    print ("Attacker's  public key -> C=root^attacksecret(mod(prime))")
    attackpublic1=(root**attacksecret1)%prime
    attackpublic2=(root**attacksecret2)%prime
    print ("Attacker public key1 which is shared with Party1: ", attackpublic1)
    print ("Attacker public key2 which is shared with Party2: ", attackpublic2)
    print('\n')
    key1=(alicepublic**attacksecret1)%prime
    key2=(bobpublic**attacksecret2)%prime
    print("The key used to decrypt message from A and modify: ",key1)
    print("The key used to encrypt message to be sent to B is: ",key2)
    return(attackpublic1,attackpublic2)
    

# Prime to be used
print ("Both parties agree to a single prime")
prime=int(input("Enter the prime number to be considered: "))

# Primitive root to be used
print ("Both must agree with single primitive root to use")
root=int(input("Enter the primitive root: "))

# Party1 chooses a secret number
alicesecret=int(input("Enter a secret number for Party1: "))

# Party2 chooses a secret number
bobsecret=int(input("Enter a secret number for Party2: "))

print('\n')
# Party1 public key A=(root^alicesecret)*mod(prime)
print ("Party1's  public key -> A=root^alicesecret(mod(prime))")
alicepublic=(root**alicesecret)%prime
print ("Party1 public key is: ",alicepublic, "\n")

# Party2 public key B=(root^bobsecret)*mod(prime)
print ("Party2's public key -> B=root^bobsecret(mod(prime))")
bobpublic=(root**bobsecret)%prime
print ("Party2 public key is", bobpublic, "\n")


# Party1 now calculates the shared key K1:
# K1 = B^(alicesecret)*mod(prime)
print ("Party1 calculates the shared key as K=B^alicesecret*(mod(prime))")
alicekey=(bobpublic**alicesecret)%prime
print ("Party1 calculates the shared key and results: ",alicekey, "\n")

# Party2 calculates the shared key K2:
# K2 = A^(bobsecret)*mod(prime)
print ("Party2 calculates the shared key as K=A^bobsecret(mod(prime))")
bobkey =(alicepublic**bobsecret)%prime
print ("Party2 calculates the shared key and results: ", bobkey, "\n")
    

#Both Alice and Bob now share a key which Eve cannot calculate
print ("Attacker does not know the shared private key that Party1 & Party2 can now use")
print("Now Eve implements Man In the Middle Attack !!")


# Party1 and Party2 exchange their public keys
# Eve(attacker) nows both parties public keys
keys=attacker(prime, root, alicepublic, bobpublic)
alicekey=(keys[0]**alicesecret)%prime
print("Party1 calculates the shared key with attacker's public key1: ")
print ("Shared final key: ",alicekey)
bobkey =(keys[1]**bobsecret)%prime
print("Party2 calculates the shared key with attacker's public key2: ")
print ("Shared final key: ", bobkey, "\n")

print("The final keys are different. ")

'''
----------OUTPUT----------
Both parties agree to a single prime
Enter the prime number to be considered: 61
Both must agree with single primitive root to use
Enter the primitive root: 43
Enter a secret number for Party1: 6756
Enter a secret number for Party2: 8356


Party1's  public key -> A=root^alicesecret(mod(prime))
Party1 public key is:  34 

Party2's public key -> B=root^bobsecret(mod(prime))
Party2 public key is 15 

Party1 calculates the shared key as K=B^alicesecret*(mod(prime))
Party1 calculates the shared key and results:  34 

Party2 calculates the shared key as K=A^bobsecret(mod(prime))
Party2 calculates the shared key and results:  34 

Attacker does not know the shared private key that Party1 & Party2 can now use
Now Eve implements Man In the Middle Attack !!
Enter a secret number1 for attacker: 7349
Enter a secret number2 for attacker: 3560


Attacker's  public key -> C=root^attacksecret(mod(prime))
Attacker public key1 which is shared with Party1:  17
Attacker public key2 which is shared with Party2:  47


The key used to decrypt message from A and modify:  9
The key used to encrypt message to be sent to B is:  47
Party1 calculates the shared key with attacker's public key1: 
Shared final key:  9
Party2 calculates the shared key with attacker's public key2: 
Shared final key:  47 

The final keys are different. 
>>> 
'''

'''
Took help from:
1. https://sublimerobots.com/2015/01/simple-diffie-hellman-example-python/
2. https://trinket.io/python/d574095364
3. https://www.wolframalpha.com/widgets/view.jsp?id=ef51422db7db201ebc03c8800f41ba99
Thanks for the help !
'''
