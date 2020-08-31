

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

print ("Party1's  public key -> A = root ^ alicesecret mod prime")
alicepublic=(root**alicesecret)%prime
print ("Party1 public key is: ",alicepublic, "\n")



# Party2 public key B=(root^bobsecret)*mod(prime)
print ("Party2's public key -> B = root ^ bobsecret mod prime")
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
print ("Party2 calculates the shared key as K = A ^ bobsecret mod prime")
bobkey =(alicepublic**bobsecret)%prime
print ("Party2 calculates the shared key and gets", bobkey, "\n")

#Both Alice and Bob now share a key which Eve cannot calculate
print ("Attacker does not know the shared private key that Party1 & Party2 can now use")


