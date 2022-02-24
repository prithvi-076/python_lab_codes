'''
Let us assume paper as the plane and a letter as a curve on the plane, 
then each letter divides the plane into regions. For example letters
"A", "D", "O", "P", "R" divide the plane into two regions so we say these 
letters each have one hole. Similarly,
letter "B" has two holes and letters such as "C", "E", "F", "K" have no holes. 
We say that the number of holes in the text is equal to the total number of 
holes in the letters of the text. Write a program to determine how many holes
are in a given text.

Sample input & output:
Enter string: HELLO STUDENTS
Number of holes in given text: 2
'''
st = input("Enter string: ")
h = 0
for i in st:
    if(i == 'A' or i == 'D' or i == 'O' or i == 'P' or i == 'Q' or i == 'R'):
        h += 1
    elif(i == 'B'):
        h += 2
print("Number of holes in given text:",h)