l=list(map(int,input("Enter numbers: ").split()))
n=[]
for i in l:
    n.append((i,pow(i,3)))
print(n)