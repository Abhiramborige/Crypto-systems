# Code for attacking on the cipher texts produced by the ceaser cipher technique
# probabilities of usage of alphabetes in english literature.
prob_of_alpha={
    'a':0.080,
    'b':0.015,
    'c':0.030,
    'd':0.040,
    'e':0.130,
    'f':0.020,
    'g':0.015,
    'h':0.060,
    'i':0.065,
    'j':0.005,
    'k':0.005,
    'l':0.035,
    'm':0.030,
    'n':0.070,
    'o':0.080,
    'p':0.020,
    'q':0.002,
    'r':0.065,
    's':0.060,
    't':0.090,
    'u':0.030,
    'v':0.010,
    'w':0.015,
    'x':0.005,
    'y':0.020,
    'z':0.002
}

cipher_text=input("Enter the cipher text to be decrypted: ")
'''
Example
cipher_text="khoor zruog"
'''
# for plain text: hello world and key 3.

# probability of frequency of alphabets in cipher text
freq_dict={}
c=cipher_text.replace(" ","")
for i in c:
    freq_dict[i]=0
for i in c:
    freq_dict[i]+=1
print("Frequency dictionary is: ")
print(freq_dict)

for i in freq_dict:
    freq_dict[i]=freq_dict[i]/len(c)

print("Frequency probabilities dictionary is: ")
print(freq_dict)
# correlation of frequency of alphabets in ciphertext with
# frequenct of corresponding letters in english

# for key i: phi(i)=summation(freq_dict[c]*prob_of_alpha[c-i])
# where c is the alphabet number [0,25]
# summation from 0 to 25

# Intuition: sum of probabilities for words in P, if i were the key

phi_arr={}
for i in range(26):
    phi_i=0
    for j in freq_dict:
        p_val=prob_of_alpha.get(chr(ord(j)-i))
        if(p_val!=None):
            phi_i+=freq_dict[j]*p_val
    phi_arr[i]=round(phi_i,4)

print("Correlation dictionary is: ")
print(phi_arr)

# sort the dictionary based on values:
phi_arr=sorted(phi_arr,key=phi_arr.get, reverse=True)

def decrypt(text,s):
    # Cipher(n) = De-cipher(26-n)
    s=26-s
    result=""
    for i in range(len(text)):
        char=text[i]
        result=result+chr((ord(char)+s-97)%26+97)
    return result

# now grab the max values from phi_arr one by one.
# the index is the key, to be used to reverse the ciphertext

print("The diciphering starts...")    
# checking in the first 10 phi_arr values:
for i in range(10):
    print("Encoded word in Caeser cipher is: ",decrypt(c,phi_arr[i]))


'''
----------OUTPUT----------
Enter the cipher text to be decrypted: khoor zruog
Frequency dictionary is: 
{'k': 1, 'h': 1, 'o': 3, 'r': 2, 'z': 1, 'u': 1, 'g': 1}
Frequency probabilities dictionary is: 
{'k': 0.1, 'h': 0.1, 'o': 0.3, 'r': 0.2, 'z': 0.1, 'u': 0.1, 'g': 0.1}
Correlation dictionary is: 
{0: 0.0482, 1: 0.0364, 2: 0.041, 3: 0.0575, 4: 0.0252, 5: 0.019, 6: 0.066, 7: 0.044, 8: 0.018, 9: 0.0242, 10: 0.0615, 11: 0.0235, 12: 0.0265, 13: 0.0395, 14: 0.037, 15: 0.0085, 16: 0.0165, 17: 0.0265, 18: 0.009, 19: 0.003, 20: 0.01, 21: 0.013, 22: 0.004, 23: 0.003, 24: 0.0015, 25: 0.008}
The diciphering starts...
Encoded word in Caeser cipher is:  ebiiltloia
Encoded word in Caeser cipher is:  axeehphkew
Encoded word in Caeser cipher is:  helloworld
Encoded word in Caeser cipher is:  khoorzruog
Encoded word in Caeser cipher is:  dahhksknhz
Encoded word in Caeser cipher is:  ifmmpxpsme
Encoded word in Caeser cipher is:  xubbemehbt
Encoded word in Caeser cipher is:  wtaadldgas
Encoded word in Caeser cipher is:  jgnnqyqtnf
Encoded word in Caeser cipher is:  yvccfnficu
>>> 
'''

