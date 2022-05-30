# Extended Euclidean algorithm for GCD(a,b)
def multi_inverse(a,b):
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
    return t1

# Chinese remainder theorem
'''
Examples:
k=3
a_array=[2,3,2]
m_array=[3,5,7]
# a_array=[3,3,0]
# m_array=[7,13,12]
# m_array=[3,4,5]
# a_array=[2,3,1]
# a_array=[6,13,9,19]
# m_array=[11,16,21,25]
'''

k=int(input("Enter the number of modular equivalent equations in the set of equations: "))
a_array=[]
m_array=[]
print("Enter the a values of the equations in serial manner")
for i in range(k):
    a_array.append(int(input()))
print("Enter the nod(m) values of the equations in serial manner")
for i in range(k):
    m_array.append(int(input()))
M=1
for i in m_array:
    M=M*i
M_array=[]
for i in m_array:
                   M_array.append(M//i)
print("The M array is: ",M_array)
M_inv_array=[]
for i in range(k):
    M_inv_array.append(multi_inverse(m_array[i],M_array[i]))
print("The M inverses are: ",M_inv_array)
x=0
for i in range(k):
    x+=a_array[i]*M_array[i]*M_inv_array[i]
print("The solution is ",x%M)


'''
----------OUTPUT----------
Enter the number of modular equivalent equations in the set of equations: 3
Enter the a values of the equations in serial manner
3
3
0
Enter the nod(m) values of the equations in serial manner
7
13
12
The M array is:  [156, 84, 91]
The table: 
0 7 156 7 1 0 0 1
22 156 7 2 0 1 1 0
3 7 2 1 1 -22 0 1
2 2 1 0 -22 67 1 -3
67 X 7 + -3 X 156 = GCD( 7 , 156 )
The evaluation is  1
The GCD of  7  and  156  is  1
INVERSE  4
The table: 
0 13 84 13 1 0 0 1
6 84 13 6 0 1 1 0
2 13 6 1 1 -6 0 1
6 6 1 0 -6 13 1 -2
13 X 13 + -2 X 84 = GCD( 13 , 84 )
The evaluation is  1
The GCD of  13  and  84  is  1
INVERSE  11
The table: 
0 12 91 12 1 0 0 1
7 91 12 7 0 1 1 0
1 12 7 5 1 -7 0 1
1 7 5 2 -7 8 1 -1
2 5 2 1 8 -15 -1 2
2 2 1 0 -15 38 2 -5
38 X 12 + -5 X 91 = GCD( 12 , 91 )
The evaluation is  1
The GCD of  12  and  91  is  1
INVERSE  7
The M inverses are:  [4, 11, 7]
The solution is  276
>>>

Took help from:
1. https://www.omnicalculator.com/math/chinese-remainder
2. https://www.dcode.fr/chinese-remainder
Thanks for the help
'''
