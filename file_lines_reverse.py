"""
Write a program to print each line of a file in reverse order. Also compute the
number of characters, words and lines in a file.
Note : file name is "kmit.txt"
Test case=1
Reverse order:
KMIT is one of the premier engineering colleges in the state of Telangana.
KMIT established in year 2007.
Keshav Memorial Institute of Technology (KMIT).
Number of lines: 3
Number of words: 24
Number of characters: 151
"""
f = open("kmit.txt","r")
l = 0
w = 0
ch = 0
for i in f:
    l += 1
    w += len(i.split())
    ch += len(i.strip())
f.close()
f = open("kmit.txt","r")
print("Reverse order:")
for i in (f.read().split("\n")[::-1]):
    print(i)
print("Number of lines:", l)
print("Number of words:", w)
print("Number of characters:", ch)
f.close()