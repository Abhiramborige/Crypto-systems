from Crypto.Util.number import *
import math
import string

main=string.ascii_lowercase

# Euclid's extended algorithm for finding the multiplicative inverse of two numbers
def multiplicative_inverse(a, m):
    a = a % m; 
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            return x 
    return 1

# Fast modular exponentiation function
def get_mod_expo(base,exponent,modulus):
    result=1
    while exponent:
        exponent=exponent//2
        d=exponent%2
        if d:
            result=result*base%modulus
        base=base*base%modulus
    return result

# Function to generate a public and private key pair
def generate_keypair(p, q):
    n=p*q
    print("Value of n: ",n)

    # Phi is the Euler's totient of n
    phi = (p-1)*(q-1)
    print("Value of phi(n): ", phi)

    # Choose an integer e such that e and phi(n) are co-prime
    # e = random.randrange(1, phi) for random pick
    print("Enter e such that is co-prime to ", phi,": ")
    e=int(input())

    # Using Euclid's Algorithm to verify that e and phi(n) are co-prime
    g=math.gcd(e,phi)
    while(g!=1):
        print("The number you entered is not co-prime")
        e=int(input())
        g=math.gcd(e,phi)
        
    print("Value of exponent(e) entered is: ", e)

    # Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)
    # Public key is (e, n) and private key is (d, n)
    return (e,n),(d,n)

# Function to Encrypt the message
def encrypt(public_key, to_encrypt):
    key, n = public_key
    
    cipher=pow(to_encrypt,key)%n
    return cipher


# Function to Decrypt the message
def decrypt(private_key, to_decrypt):
    key, n = private_key
    
    decrypted=pow(to_decrypt,key)%n
    return decrypted

# Main Program
p=getPrime(6)
print("Randomly generated prime number p: ",p)
q=getPrime(6)
print("Randomly generated prime number q: ",q)

print("Generating Public/Private key-pairs!")
public, private = generate_keypair(p, q)
print("Your public key is (e,n) ", public)
print("Your private key is (d,n) ", private)

message = input("Enter the message: ")
arr=[]
cipher_text=[]
for i in message:
    if i in main:
        arr.append(main.index(i))
for i in arr:
    cipher_text.append(encrypt(public,i))

print("Encrypted message (Cipher Text): ",cipher_text)

plain=[]
for i in cipher_text:
    plain.append(decrypt(private,i))
plain_text=''
for i in plain:
    plain_text=plain_text+main[i]
print("Plain text array: ",plain)
print("Decrypted message (Plain Text): ", plain_text)
