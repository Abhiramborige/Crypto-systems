
# this function is to get the desired sequence
def sequence(n):
    arr=[]
    i=0
    # creating the sequence required for
    # implementing railfence cipher
    # the sequence is stored in array
    while(i<n-1):
        arr.append(i)
        i+=1
    while(i>0):
        arr.append(i)
        i-=1
    return(arr)

# this is to implement the logic
def railfence(cipher_text,n):
    # converting into lower cases
    cipher_text=cipher_text.lower()

    # If you want to remove spaces,
    # you can uncomment this
    # s=s.replace(" ","")

    # returning the sequence here
    L=sequence(n)
    print("The raw sequence of indices: ",L)

    # storing L in temp for reducing additions in further steps
    # if not stored and used as below, the while loop
    # will create L of excess length
    temp=L
    
    # adjustments
    while(len(cipher_text)>len(L)):
        L=L+temp

    # removing the extra last indices
    for i in range(len(L)-len(cipher_text)):
        L.pop()
        
    # storing L.sort() in temp1
    temp1=sorted(L)
    
    print("The row indices of the characters in the cipher string: ",L)

    print("The row indices of the characters in the plain string: ",temp1)
    
    print("Transformed message for decryption: ",cipher_text)

    # converting into plain text
    plain_text=""
    for i in L:
        # k is index of particular character in the cipher text
        # k's value changes in such a way that the order of change
        # in k's value is same as plaintext order
        k=temp1.index(i)
        temp1[k]=n
        plain_text+=cipher_text[k]
        
    print("The cipher text is: ",plain_text)


cipher_text=input("Enter the string to be decrypted: ")
n=int(input("Enter the number of rails: "))
railfence(cipher_text,n)

'''
----------OUTPUT----------
Enter the string to be decrypted: hyeaerov dyyenag  vehode o
Enter the number of rails: 5
The raw sequence of indices:  [0, 1, 2, 3, 4, 3, 2, 1]
The row indices of the characters in the cipher string:  [0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1]
The row indices of the characters in the plain string:  [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 4, 4, 4]
Transformed message for decryption:  hyeaerov dyyenag  vehode o
The cipher text is:  hey everyone have good day
>>> 
'''

