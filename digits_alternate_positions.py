'''
Difference of the sum of alternate digits: Given a positive integer 'x' (with even number of digits in
it), compute the difference between the sum of the digits occurring in the alternate positions (starting
from the first position) and the sum of the digits occurring in the alternate positions, starting from the
last rightmost position of 'x'.
'''
n=input("Enter an integer: ")
s1,s2=0,0
for i in range(len(n)):
    if (i%2==0):
        s1=s1+int(n[i])
    else:
        s2=s2+int(n[i])
if(len(n)%2==0):
    print(f"Difference between the sums of the digits occurring in the alternate positions: {abs(s1-s2)}")
else:
    print("Invalid number")