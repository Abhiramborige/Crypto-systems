import math

def row(s,key):

    # to remove repeated alphabets in key
    temp=[]
    for i in key:
        if i not in temp:
            temp.append(i)
    k=""
    for i in temp:
        k+=i
    print("The key used for encryption is: ",k)
    
    arr=[['' for i in range(len(k))]
         for j in range(int(len(s)/len(k)))]

    # To get indices as the key numbers instead of alphabets in the key, according
    # to algorithm, for appending the elementsof matrix formed earlier, column wise.
    kk=sorted(k)
    
    d=0
    # arranging the cipher message into matrix
    # to get the same matrix as in encryption
    for i in kk:
        h=k.index(i)
        for j in range(len(k)):
            arr[j][h]=s[d]
            d+=1
                
    print("The message matrix is: ")
    for i in arr:
        print(i)

    # the plain text
    plain_text=""
    for i in arr:
        for j in i:
            plain_text+=j
    print("The plain text is: ",plain_text)

        
msg=input("Enter the message to be decrypted: ")
key=input("Enter the key in alphabets: ")
row(msg,key)

'''
----------OUTPUT----------
Enter the message to be decrypted: Mu b___mid____crnm___ ew ___o ee___ps ____ytoy___
Enter the key in alphabets: expensive
The key used for encryption is:  expnsiv
The message matrix is: 
['M', 'y', ' ', 'c', 'o', 'm', 'p']
['u', 't', 'e', 'r', ' ', 'i', 's']
[' ', 'o', 'w', 'n', 'e', 'd', ' ']
['b', 'y', ' ', 'm', 'e', '_', '_']
['_', '_', '_', '_', '_', '_', '_']
['_', '_', '_', '_', '_', '_', '_']
['_', '_', '_', '_', '_', '_', '_']
The plain text is:  My computer is owned by me_______________________
>>>
'''
