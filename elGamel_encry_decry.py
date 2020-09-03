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
    members=groupMembers(p)
    factors=[]
    print("Euler's toutient function value: ")
    print("Phi(p): ",len(members))
    for i in range(1,len(members)+1):
        if(len(members)%i==0):
            factors.append(i)
    c=[]
    for i in members:
        ar=[]
        for j in factors:
            if(pow(i,j)%p==1):
                ar.append(j)
        if(len(ar)==0):
            c.append(0)
        else:
            c.append(min(ar))        
    return(c)

p=int(input("Enter a large prime number: "))
members=groupMembers(p)
print("The members in the group  Zp* are: ",members)

# d to be a member of the Zp* 
d=int(input("Select a number from the array as d(private key): "))
if(d not in members or d>p-2):
    print("Entered wrong number")
    
else:
    primitives=[]
    powers=PrimitiveRoots(p)

    # finding primitives from powers
    # Used Legrange's theorem
    for i in powers:
        if(i==len(members)):
            primitives.append(members[powers.index(i)])
            powers[powers.index(i)]=0
            
    # e1 is primitive root in Zp*
    print("The list of primitive roots are: ",primitives)
    e1=int(input("Enter the primitive root of Zp*: "))
    if(e1 not in primitives):
        print("Entered wrong number")
        
    else:
        e2=pow(e1,d)%p
        print("Public key (e1,e2,p): ",e1," ",e2," ",p)
        print("Private key (d): ",d)

        # Encryption
        print("Enter an integer from Zp*: ", members)
        r=int(input())
        if(r not in members):
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
Enter a large prime number: 53
The members in the group  Zp* are:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]
Select a number from the array as d(private key): 36
Euler's toutient function value: 
Phi(p):  52
The list of primitive roots are:  [2, 3, 5, 8, 12, 14, 18, 19, 20, 21, 22, 26, 27, 31, 32, 33, 34, 35, 39, 41, 45, 48, 50, 51]
Enter the primitive root of Zp*: 50
Public key (e1,e2,p):  50   46   53
Private key (d):  36
Enter an integer from Zp*:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]
31
Enter the message in numbers: 48
Encrypted message (C1):  31
Encrypted message (C2):  30
Decrypted message is:  48
>>> 
'''

'''
Note: The message to be encrypted must be less than the prime value given initially
Took help from: 
1. https://www.wolframalpha.com/widgets/view.jsp?id=ef51422db7db201ebc03c8800f41ba99
2. https://en.wikipedia.org/wiki/Primitive_root_modulo_n
Thanks for the help !
'''
