import string


main=string.ascii_lowercase

def generate_key(n,s):
    s=s.replace(" ","")
    s=s.lower()
    
    key_matrix=['' for i in range(n)]
    i=0;j=0
    for c in s:
        if c in main:
            key_matrix[i]+=c
            j+=1
            if(j>n-1):
                i+=1
                j=0
    print("The key matrix "+"("+str(n)+'x'+str(n)+") is:")
    print(key_matrix)
    
    key_num_matrix=[]
    for i in key_matrix:
        sub_array=[]
        for j in range(n):
            sub_array.append(ord(i[j])-ord('a'))
        key_num_matrix.append(sub_array)
        
    for i in key_num_matrix:
        print(i)
    return(key_num_matrix)
    

def message_matrix(s,n):
    s=s.replace(" ","")
    s=s.lower()
    final_matrix=[]
    if(len(s)%n!=0):
        # z is the bogus word
        while(len(s)%n!=0):
            s=s+'z'
    print("Converted plain_text for encryption: ",s)
    for k in range(len(s)//n):
        message_matrix=[]
        for i in range(n):
            sub=[]
            for j in range(1):
                sub.append(ord(s[i+(n*k)])-ord('a'))
            message_matrix.append(sub)
        final_matrix.append(message_matrix)
    print("The column matrices of plain text in numbers are:  ")
    for i in final_matrix:
        print(i)
    return(final_matrix)


# Function to get cofactor of  
# mat[p][q] in temp[][]
# passing the key matrix as 'mat' to check for invertibility
def getCofactor(mat, temp, p, q, n): 
    i = 0
    j = 0
  
    # Looping for each element 
    # of the matrix 
    for row in range(n):  
        for col in range(n): 
              
            # Copying into temporary matrix only those element   
            # which are not in given row and column 
            if (row != p and col != q) : 
                temp[i][j] = mat[row][col] 
                j += 1
  
                # Row is filled, so increase  
                # row index and reset col index 
                if (j == n - 1): 
                    j = 0
                    i += 1
  
# Recursive function for finding determinant of matrix. 
# n is current dimension of mat[][].  
def determinantOfMatrix(mat, n): 
    D = 0 # Initialize result 
  
    # Base case : if matrix  
    # contains single element 
    if (n == 1): 
        return mat[0][0] 
          
    # To store cofactors 
    temp = [[0 for x in range(n)]  
               for y in range(n)]  
  
    sign = 1 # To store sign multiplier 
  
    # Iterate for each  
    # element of first row 
    for f in range(n): 
          
        # Getting Cofactor of mat[0][f] 
        getCofactor(mat, temp, 0, f, n) 
        D += (sign * mat[0][f] *
              determinantOfMatrix(temp, n - 1)) 
  
        # terms are to be added with alternate sign 
        sign = -sign 
    return D 
  
def isInvertible(mat, n): 
    if (determinantOfMatrix(mat, n) != 0): 
        return True
    else: 
        return False


def multiply_and_convert(key,message):
    
    # multiplying matrices
    # resultant must have:
    # rows = numbers of rows in message matrix
    # columns = number of columns in key matrix 
    res_num = [[0 for x in range(len(message[0]))] for y in range(len(key))]
    
    for i in range(len(key)): 
        for j in range(len(message[0])):
            for k in range(len(message)): 
                # resulted number matrix
                res_num[i][j]+=key[i][k] * message[k][j]

    res_alpha = [['' for x in range(len(message[0]))] for y in range(len(key))]
    # getting the alphabets from the numbers
    # according to the logic of hill ciipher
    for i in range(len(key)):
        for j in range(len(message[0])):
            # resultant alphabet matrix
            res_alpha[i][j]+=chr((res_num[i][j]%26)+97)
            
    return(res_alpha)

# implementing all logic and calling function
n=int(input("What will be the order of square matrix: "))
s=input("Enter the key: ")
key=generate_key(n,s)

# check for invertability here
if (isInvertible(key, len(key))): 
    print("Yes it is invertable and can be decrypted") 
else: 
    print("No it is not invertable and cannot be decrypted")
    
plain_text=input("Enter the message: ")
message=message_matrix(plain_text,n)
final_message=''
for i in message:
    sub=multiply_and_convert(key,i)
    for j in sub:
        for k in j:
            final_message+=k
print("plain message: ",plain_text)
print("final encrypted message: ",final_message)

'''
----------OUTPUT----------
What will be the order of square matrix: 3
Enter the key: BACK UP ABC
The key matrix (3x3) is:
['bac', 'kup', 'abc']
[1, 0, 2]
[10, 20, 15]
[0, 1, 2]
Yes it is invertable and can be decrypted
Enter the message: hi there my name is abhiram
Converted plain_text for encryption:  hitheremynameisabhiramzz
The column matrices of plain text in numbers are:  
[[7], [8], [19]]
[[7], [4], [17]]
[[4], [12], [24]]
[[13], [0], [12]]
[[4], [8], [18]]
[[0], [1], [7]]
[[8], [17], [0]]
[[12], [25], [25]]
plain message:  hi there my name is abhiram
final encrypted message:  tvuppmaqilyyocsovpierkhx
>>> 
'''
                
            
