# S-box Table
# We have 8 different 4x16 matrices for each S box
#It converts 48 bits to 32 bits
# Each S box will get 6 bits and output will be 4 bits
s_box = [
        [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
         [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
         [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
         [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
        [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
         [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
         [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
         [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],
        [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
         [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
         [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
         [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
        [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
         [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
         [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
         [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
        [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
         [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
         [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
         [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],
        [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
         [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
         [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
         [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],
        [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
         [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
         [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
         [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
        [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
         [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
         [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
         [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
      ]

# Round count: 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
# Bits shifted:1 1 2 2 2 2 2 2 1  2  2  2  2  2  2  1
# Number of bit shifts  
shift_table=[1, 1, 2, 2, 
            2, 2, 2, 2, 
            1, 2, 2, 2, 
            2, 2, 2, 1 ] 

# Initial Permutation Table: (input of 64bit block size is pasesed: 64bit -> 64bit)
initial_perm = [58, 50, 42, 34, 26, 18, 10, 2,  
                60, 52, 44, 36, 28, 20, 12, 4,  
                62, 54, 46, 38, 30, 22, 14, 6,  
                64, 56, 48, 40, 32, 24, 16, 8,  
                57, 49, 41, 33, 25, 17, 9, 1,  
                59, 51, 43, 35, 27, 19, 11, 3,  
                61, 53, 45, 37, 29, 21, 13, 5,  
                63, 55, 47, 39, 31, 23, 15, 7]  

# Permuted choice 1: (key is passed: 64bit -> 56bit)
# That is bit position 8, 16, 24, 32, 40, 48, 56 and 64 are discarded from the key.
perm_cho_1= [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18,
             10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36,
             63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22,
             14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]

# Permuted choice 2: (key is passed into it after applying 
# left shift to both halves: 56bit -> 56bit)
perm_cho_2= [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10,
            23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2,
            41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48,
            44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]

# Expansion permutation table
expan_perm=[32, 1, 2, 3, 4, 5,
            4, 5, 6, 7, 8, 9,
            8, 9, 10, 11, 12, 13,
            12, 13, 14, 15, 16, 17, 
            16, 17, 18, 19, 20, 21,
            20, 21, 22, 23, 24, 25,
            24, 25, 26, 27, 28, 29,
            28, 29, 30, 31, 32, 1]

# Permutation table 
perm_table=[16, 7, 20, 21, 29, 12, 28, 17,
            1, 15, 23, 26, 5, 18, 31, 10,
            2, 8, 24, 14, 32, 27, 3, 9,
            19, 13, 30, 6, 22, 11, 4, 25]

# Final Permutaion Table
final_perm = [40, 8, 48, 16, 56, 24, 64, 32, 
              39, 7, 47, 15, 55, 23, 63, 31, 
              38, 6, 46, 14, 54, 22, 62, 30,
              37, 5, 45, 13, 53, 21, 61, 29, 
              36, 4, 44, 12, 52, 20, 60, 28, 
              35, 3, 43, 11, 51, 19, 59, 27, 
              34, 2, 42, 10, 50, 18, 58, 26, 
              33, 1, 41, 9, 49, 17, 57, 25 ] 

# XOR function
def xor(a,b): 
  # a and b should be in binary
  ans="" 
  for i in range(len(a)): 
    if(a[i]==b[i]): 
      ans=ans+"0"
    else: 
      ans=ans+"1"
  return ans

# Hexadecimal to binary conversion 
def hexa_to_bin(msg): 
  mp = {'0' : "0000",  
        '1' : "0001", 
        '2' : "0010",  
        '3' : "0011", 
        '4' : "0100", 
        '5' : "0101",  
        '6' : "0110", 
        '7' : "0111",  
        '8' : "1000", 
        '9' : "1001",  
        'A' : "1010", 
        'B' : "1011",  
        'C' : "1100", 
        'D' : "1101",  
        'E' : "1110", 
        'F' : "1111" } 
  bin = "" 
  for i in range(len(msg)): 
    bin = bin + mp[msg[i]] 
  return bin
    
# Binary to hexadecimal conversion 
def bin_to_hexa(msg): 
  mp = {"0000" : '0',  
        "0001" : '1', 
        "0010" : '2',  
        "0011" : '3', 
        "0100" : '4', 
        "0101" : '5',  
        "0110" : '6', 
        "0111" : '7',  
        "1000" : '8', 
        "1001" : '9',  
        "1010" : 'A', 
        "1011" : 'B',  
        "1100" : 'C', 
        "1101" : 'D',  
        "1110" : 'E', 
        "1111" : 'F' } 
  hex="" 
  for i in range(0,len(msg),4): 
    ch="" 
    ch=ch+msg[i] 
    ch=ch+msg[i+1]  
    ch=ch+msg[i+2]  
    ch=ch+msg[i+3]  
    hex=hex+mp[ch] 
  return hex
  
# Binary to decimal conversion 
def bin_to_dec(msg):  
  decimal,i=0,0
  while(msg!=0):  
    dec=msg%10
    decimal=decimal+dec*pow(2, i)  
    msg=msg//10
    i+=1
  return decimal 
  
# Decimal to binary conversion 
def dec_to_bin(num):  
  res=bin(num).replace("0b", "") 
  if(len(res)%4 != 0): 
    div=len(res) / 4
    div=int(div) 
    counter=(4*(div+1))-len(res)  
    for i in range(0, counter): 
      res='0'+res 
  return res

# shifting the bits towards left by nth shifts 
def shift_left(key,nth_shifts): 
  s="" 
  for i in range(nth_shifts): 
    for j in range(1,len(key)): 
      s=s+key[j] 
    s=s+key[0] 
    key=s 
    s=""  
  return key

# Step1: It is just rearranging the positions of all bits of plain text
# according to the initial_perm matrix(8x8)
def initial_permutation(plain_text,initial_perm, no_bits): 
  permutation="" 
  for i in range(0,no_bits): 
    permutation=permutation+plain_text[initial_perm[i]-1] 
  return permutation 

# Encryption function is implemented here
def encrypt(msg,key):
  print("Encryption")
  msg=hexa_to_bin(msg)
  msg = initial_permutation(msg, initial_perm, 64) 
  print("Message after initial permutation: ",bin_to_hexa(msg))
  # converting from hexa to binary
  key = hexa_to_bin(key) 

  key = initial_permutation(key, perm_cho_1, 56)
  print("The converted 56bit key is: ",key)
  # Halving the key
  l=key[0:28]
  r=key[28:56]
  # Halving the message
  left = msg[0:32] 
  right =msg[32:64] 

  # Key transformation
  key_from_pc2_bin=[]
  key_from_pc2_hex=[]
  for k in range(16):
    l=shift_left(l,shift_table[k])
    r=shift_left(r,shift_table[k])
    combine_key=l+r
    
    # permuted choice 2
    round_key=initial_permutation(combine_key,perm_cho_2,48)
    key_from_pc2_bin.append(round_key)
    key_from_pc2_hex.append(bin_to_hexa(round_key))
  
  # For decryption, just uncomment below two lines
  # key_from_pc2_bin=key_from_pc2_bin[::-1]
  # key_from_pc2_hex=key_from_pc2_hex[::-1]  

  # Message transformation
  # Encryption
  print()
  
  print("Round: Left key part: Right key part: SubKey used:")
  for j in range(16):
    # Expansion Permutation
    right_expand=initial_permutation(right,expan_perm,48)
    xor_x=xor(right_expand,key_from_pc2_bin[j])

    # calculating row and column from s box
    s_box_str="" 
    for i in range(0,8):
      row=bin_to_dec(int(xor_x[i*6]+xor_x[i*6+5]))
      col=bin_to_dec(int(xor_x[i*6+1]+xor_x[i*6+2]+xor_x[i*6+3]+xor_x[i*6+4]))
      val=s_box[i][row][col]
      s_box_str=s_box_str+dec_to_bin(val)

    # towards permutation box
    s_box_str=initial_permutation(s_box_str,perm_table,32)

    # Now again XOR with left part and above
    result=xor(left,s_box_str)
    left=result

    
    # Swapping
    if(j!=15):
      left, right=right, left
    print(str(j+1).zfill(2),"     ",bin_to_hexa(left),"      ",bin_to_hexa(right),"   ",key_from_pc2_hex[j])

  # concatinating both left and right
  combine=left+right
  cipher_text=initial_permutation(combine,final_perm,64)
  return cipher_text

# Padding function
def pad(msg):
  if(len(msg)%16!=0):
    print("Padding required")
    for i in range(abs(16-(len(msg)%16))):
      msg=msg+'0'
  else:
    print("No padding required")
  return(msg)

# Main function
print("Enter the message to be encrypted: ")
plain_text=input()
plain_text=pad(plain_text)
print("Message after padding: ", plain_text)
  
print("Enter the 64bit key for encryption: ")
key=input()
key=pad(key)
print("Key after padding: ",key)

cipher_text=bin_to_hexa(encrypt(plain_text,key))
print("Cipher text is: ",cipher_text)

'''
----------OUTPUT----------
Enter the message to be encrypted: 
536ABCD8910FF9
Padding required
Message after padding:  536ABCD8910FF900
Enter the 64bit key for encryption: 
74631BBDCA8
Padding required
Key after padding:  74631BBDCA800000
Encryption
Message after initial permutation:  4B5D24715C466E23
The converted 56bit key is:  00111000000100110000101100000001011000001001000111001101

Round: Left key part: Right key part: SubKey used:
01       5C466E23        6E81D6DE     A289056D34C0
02       6E81D6DE        8F2C919D     8A34034AB231
03       8F2C919D        7C74DB60     69064C734D28
04       7C74DB60        69DDF400     40D08808191A
05       69DDF400        44AE2868     108972C57034
06       44AE2868        B2467F7F     A46803610AE8
07       B2467F7F        458145D1     23270490981F
08       458145D1        488D0D53     4814910716B4
09       488D0D53        62E16561     494060887282
10       62E16561        0A6342EC     80C9B8746225
11       0A6342EC        EA0DAA35     942303B208CA
12       EA0DAA35        7669590A     231E0184B313
13       7669590A        5706FABD     4930C4372660
14       5706FABD        29B656BD     10C4D8788942
15       29B656BD        31FA5C5F     54412204E41E
16       6A1A9764        31FA5C5F     16AB20801DC9
Cipher text is:  86760F7ABEE16B24
>>> 
'''

'''
For decryption, we have to add just two lines, which server the purpose of 
reversing the array, which stores the sub keys for different rounds

For decryption, just we have to reverse the array which stores the sub keys:
key_from_pc2_bin=key_from_pc2_bin[::-1]
key_from_pc2_hex=key_from_pc2_hex[::-1]
'''

'''
----------OUTPUT----------
Enter the message to be decrypted: 
86760F7ABEE16B24
No padding required
Message after padding:  86760F7ABEE16B24
Enter the 64bit key for decryption: 
74631BBDCA8
Padding required
Key after padding:  74631BBDCA800000
Encryption
Message after initial permutation:  6A1A976431FA5C5F
The converted 56bit key is:  00111000000100110000101100000001011000001001000111001101
Round: Left key part: Right key part: SubKey used:
01       31FA5C5F        29B656BD     16AB20801DC9
02       29B656BD        5706FABD     54412204E41E
03       5706FABD        7669590A     10C4D8788942
04       7669590A        EA0DAA35     4930C4372660
05       EA0DAA35        0A6342EC     231E0184B313
06       0A6342EC        62E16561     942303B208CA
07       62E16561        488D0D53     80C9B8746225
08       488D0D53        458145D1     494060887282
09       458145D1        B2467F7F     4814910716B4
10       B2467F7F        44AE2868     23270490981F
11       44AE2868        69DDF400     A46803610AE8
12       69DDF400        7C74DB60     108972C57034
13       7C74DB60        8F2C919D     40D08808191A
14       8F2C919D        6E81D6DE     69064C734D28
15       6E81D6DE        5C466E23     8A34034AB231
16       4B5D2471        5C466E23     A289056D34C0
Plain text is:  536ABCD8910FF900
>>> 
'''

'''
Took help from: https://www.geeksforgeeks.org/data-encryption-standard-des-set-1
Thanks for the help !
'''
