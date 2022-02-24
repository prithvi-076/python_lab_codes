'''
Sample input & output 1:
Enter a number which contains only digits 0's and 1's: 101011
NO
Sample input & output 2:
Enter a number which contains only digits 0's and 1's: 1111101
YES
Sample input & output 3:
Enter a number which contains only digits 0's and 1's: 0001000
YES
'''
def canmakeall(st):
    z = 0
    one = 0
    for i in range(len(st)):
        ch = st[i]
        if(ch == 0):
            z += 1
        elif(ch == 1):
            one += 1
    return(z == 1 or one == 1)
st = input("Enter a number which contains only digits 0's and 1's: ")
if(canmakeall(st)):
    print("YES")
else:
    print("NO")