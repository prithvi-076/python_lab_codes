import math
n = int(input("Enter an integer:"))
i = math.floor(n/4) - 1
if(4*i+6==n):
    print(f"{n} is a Consecutive Four Sum Number")
else:
    print(f"{n} is not a Consecutive Four Sum Number")