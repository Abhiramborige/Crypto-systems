# importing tinyec module
import tinyec.ec as ec

# parameters are prime field, (Generator point G), order and cofactor
# The order of the curve is the total number of all EC points on the curve.
# This total number of points includes also the special point called 
# "point at infinity", which is obtained when a point is multiplied by 0.

# The order of entire group is n = h * r (the number of subgroups,
# multiplied by the number of points in each subgroup).
# The number of subgroups h holding the EC points is called cofactor.

# Pre-defined values for My_curve
p=97
g=(37, 71)
n=14
h=1
name="My_curve"
a=2
b=1

# We can also use pre defined curves in registry class
'''
1. brainpoolP160r1
2. brainpoolP192r1
3. brainpoolP224r1
4. brainpoolP256r1
5. brainpoolP320r1
6. brainpoolP384r1
7. brainpoolP512r1
8. secp192r1
9. secp224r1
10. secp256r1
11. secp384r1
12. secp521r1
'''
# Example: curve = registry.get_curve('brainpoolP256r1')

field = ec.SubGroup(p=p, g=g, n=n, h=h)
curve = ec.Curve(a=a, b=b, field=field, name=name)

print('The curve is:')
print(curve)
print("Generator point is: ")
print(curve.g)
print("The integer points possible on the curve are: ")
for k in range(0, 14):
    p = k * curve.g
    print(str(k).zfill(2),"*","G = ",(p.x,p.y))

print()
# User A select private key:
n_a = n
while(n_a >= n):
    n_a=int(input("Enter A's private key(less than n): "))

# User B select private key:
n_b = n
while(n_b >= n):
    n_b=int(input("Enter B's private key(less than n): "))

# User A public key
P_a=n_a*curve.g

# User B public key
P_b=n_b*curve.g

print()
print("The public keys are: ")
print(P_a)
print(P_b)

# Secret key by user A(sender):
K_a=n_a*P_b

# Secret key by user B(receiver):
K_b=n_b*P_a

print("Secret key on User A: ",K_a)
print("Secret key on User B: ",K_b)

# On sender's side
K_a=ec.Point(curve, K_a.x, K_a.y)
Message=input("Enter the x and y coordinates by space seperated: ")
Message=list(map(int, Message.split(" ")))
message_point=ec.Point(curve, Message[0], Message[1])

# k is a random number
k=int(input("Enter a random number: "))

Cipher_point_x = k * curve.g
print("Cipher text 1st component(point on My_curve): ",Cipher_point_x)
Cipher_point_y = message_point + k * P_b
print("Cipher text 2nd component(point on My_curve): ",Cipher_point_y)

# On receiver's side
Plain_point = Cipher_point_x * n_b
Plain_point = (message_point + k * P_b) - Plain_point
print("The plain text point after decryption, corresponding to a point on curve is: ")
print(Plain_point)
