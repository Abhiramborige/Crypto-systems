
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
def railfence(s,n):
    # converting into lower cases
    s=s.lower()

    # If you want to remove spaces,
    # you can uncomment this
    # s=s.replace(" ","")

    # returning the sequence here
    L=sequence(n)
    print("The raw sequence of indices: ",L)

    # storing L in temp for reducing additions in further steps
    temp=L
    
    # adjustments
    while(len(s)>len(L)):
        L=L+temp

    # removing the extra last indices
    for i in range(len(L)-len(s)):
        L.pop()
    print("The row indices of the characters in the given string: ",L)
    
    
    print("Transformed message for encryption: ",s)

    # converting into cipher text
    num=0
    cipher_text=""
    while(num<n):
        for i in range(L.count(num)):
            # adding characters according to
            # indices to get cipher text
            cipher_text=cipher_text+s[L.index(num)]
            L[L.index(num)]=n
        num+=1
    print("The cipher text is: ",cipher_text)
   
plain_text=input("Enter the string to be encrypted: ")
n=int(input("Enter the number of rails: "))
railfence(plain_text,n)

'''
----------OUTPUT----------
Enter the string to be encrypted: Hey everyone have good day
Enter the number of rails: 5
The raw sequence of indices:  [0, 1, 2, 3, 4, 3, 2, 1]
The row indices of the characters in the given string:  [0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1]
Transformed message for encryption:  hey everyone have good day
The cipher text is:  hyeaerov dyyenag  vehode o
>>>
'''

