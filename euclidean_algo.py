# Euclidean algorithm for GCD(a,b)

a=int(input("Enter a: "))
b=int(input("Enter b: "))
'''
Example
a=1331
b=13
'''

r1=a
r2=b
while(r2>0):
    quo=r1//r2
    rem=r1%r2
    print(quo,r1,r2,rem)
    r1=r2
    r2=rem

print("The GCD of ",a, " and ",b," is ",r1)

'''
----------OUTPUT----------
Enter a: 1331
Enter b: 13
102 1331 13 5
2 13 5 3
1 5 3 2
1 3 2 1
2 2 1 0
The GCD of  1331  and  13  is  1
>>>

Took help from: https://www.extendedeuclideanalgorithm.com/calculator.php
Thanks for the help!
'''
