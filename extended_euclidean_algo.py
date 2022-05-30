# Extended Euclidean algorithm for GCD(a,b)

a=int(input("Enter a: "))
b=int(input("Enter b: "))
'''
b.mod(a)
Example
a=1331
b=13
'''

r1=a
r2=b
s1=1
s2=0
t1=0
t2=1
print("The table: ")
while(r2>0):
    quo=r1//r2;
    rem=r1%r2
    print(quo, r1, r2, rem, s1, s2, t1, t2)
    r1=r2
    r2=rem
    s=s1-quo*s2
    s1=s2
    s2=s
    t=t1-quo*t2
    t1=t2
    t2=t
print(s1,"X",a,"+",t1,"X",b,"= GCD(",a,",",b,")")
print("The evaluation is ",s1*a+t1*b)
print("The GCD of ",a, " and ",b," is ",r1)
if(r1==1):
    if(t1>0):
        print("INVERSE ",t1)
    else:
        while(t1<0):
            t1+=a
        print("INVERSE ",t1)
else:
    print("Inverse doesnt exist")

'''
----------OUTPUT----------
Enter a: 1331
Enter b: 13
The table: 
102 1331 13 5 1 0 0 1
2 13 5 3 0 1 1 -102
1 5 3 2 1 -2 -102 205
1 3 2 1 -2 3 205 -307
2 2 1 0 3 -5 -307 512
-5 X 1331 + 512 X 13 = GCD( 1331 , 13 )
The evaluation is  1
The GCD of  1331  and  13  is  1
INVERSE  512
>>>

Took help from: https://www.extendedeuclideanalgorithm.com/calculator.php
Thanks for the help!
'''
