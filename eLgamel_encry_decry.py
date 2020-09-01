def gcd(a,b): 
    if (a==0): 
        return b; 
    return gcd(b%a,a); 
  
# Function to return members of group Zn* 
def groupMembers(n):
    arr=[]
    # 1 is always a generator and member
    for i in range(1, n): 
        # Checking relative prime nature
        if (gcd(i,n)==1): 
            arr.append(i)
    return arr

# Function to return the primitive roots modulo p (Zp*)
def PrimitiveRoots(p): 
    arr=[]
    members=groupMembers(p)
    factors=[]
    for i in range(1,len(members)+1):
        if(len(members)%i==0):
            factors.append(i)
    for i in members:
        for j in factors:
            if(pow(i,j)%p==1 and j==len(members)):
                arr.append(i)
    return list(set(arr))

p=int(input("Enter a large prime number: "))
print("The members in the group  Zp* are: ",groupMembers(p))

# d to be a member of the Zp* 
d=int(input("Select a number from the array as d(private key): "))
if(d not in groupMembers(p) or d>p-2):
    print("Entered wrong number")
    
else:
    
    # e1 is primitive root in Zp*
    print("The list of primitive roots are: ",PrimitiveRoots(p))
    e1=int(input("Enter the primitive root in Zp*: "))
    if(e1 not in PrimitiveRoots(p)):
        print("Entered wrong number")
        
    else:
        e2=pow(e1,d)%p
        print("Public key (e1,e2,p): ",e1," ",e2," ",p)
        print("Private key (d): ",d)

        # Encryption
        print("Enter an integer from Zp*: ", groupMembers(p))
        r=int(input())
        if(r not in groupMembers(p)):
            print("Entered wrong number")
            
        else:
            C1=pow(e1,r)%p
            message=int(input("Enter the message in numbers: "))
            C2=(message*pow(e2,r))%p

            # Decryption:
            P=(pow(C1,p-d-1)*C2)%p

            print("Encrypted message (C1): ",C1)
            print("Encrypted message (C2): ",C2)
            print("Decrypted message is: ",P)


'''
----------OUTPUT----------
Enter a large prime number: 29
The members in the group  Zp* are:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
Select a number from the array as d(private key): 18
The list of primitive roots are:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
Enter the primitive root in Zp*: 23
Public key (e1,e2,p):  23   20   29
Private key (d):  18
Enter an integer from Zp*:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
22
Enter the message in numbers: 17
Encrypted message (C1):  23
Encrypted message (C2):  21
Decrypted message is:  17
>>> 
'''

'''
Took help from: 
https://www.geeksforgeeks.org/find-the-number-of-primitive-roots-modulo-prime/
Thanks for the help !
'''
