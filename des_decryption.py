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
    
  key_from_pc2_bin=key_from_pc2_bin[::-1]
  key_from_pc2_hex=key_from_pc2_hex[::-1]
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
  plain_text=initial_permutation(combine,final_perm,64)
  return plain_text
    

# Main function
print("Enter the 64bit message to be decrypted: ")
cipher_text=input()
print("Enter the 64bit key for decryption: ")
key=input()

plain_text=bin_to_hexa(encrypt(plain_text,key))
print("Plain text is: ",plain_text)

'''
----------OUTPUT----------
Enter the 64bit message to be decrypted: 
C0B7A8D05F3A829C
Enter the 64bit key for decryption: 
AABB09182736CCDD
Encryption
Message after initial permutation:  19BA9212CF26B472
The converted 56bit key is:  11000011110000000011001110100011001111110000110011111010

Round: Left key part: Right key part: SubKey used:
01       CF26B472        BD2DD2AB     181C5D75C66D
02       BD2DD2AB        387CCDAA     3330C5D9A36D
03       387CCDAA        22A5963B     251B8BC717D0
04       22A5963B        FF3C485F     99C31397C91F
05       FF3C485F        6CA6CB20     C2C1E96A4BF3
06       6CA6CB20        10AF9D37     6D5560AF7CA5
07       10AF9D37        308BEE97     02765708B5BF
08       308BEE97        A9FC20A3     84BB4473DCCC
09       A9FC20A3        2E8F9C65     34F822F0C66D
10       2E8F9C65        A15A4B87     708AD2DDB3C0
11       A15A4B87        236779C2     C1948E87475E
12       236779C2        B8089591     69A629FEC913
13       B8089591        4A1210F6     DA2D032B6EE3
14       4A1210F6        5A78E394     06EDA4ACF5B5
15       5A78E394        18CA18AD     4568581ABCCE
16       14A7D678        18CA18AD     194CD072DE8C
Plain text is:  123456ABCD132536
'''

