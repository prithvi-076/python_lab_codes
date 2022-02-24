'''
Program 1
Consider a situation where you want to find if the student is present or not in the class.
Iterate over a list of student names and print all the names
until you find the student name you are searching for.

TestCase 1:
Enter students names :ramu sita laxman bharath hanuma kshatragna ramayan
Enter name to search :hanuma
ramu
sita
laxman
bharath
hanuma
hanuma present at position : 5
Stopped the search
loop has ended 
TestCase 2:
Enter students names :ramu sita laxman bharath hanuma kshatragna ramayan
Enter name to search :mahabharat
ramu
sita
laxman
bharath
hanuma
kshatragna
ramayan
student with name mahabharat not present
loop has ended
'''
my_list=list(map(str,input("Enter students names :").split()))
search_name=input("Enter name to search :")
count = 0
for i in my_list:
    count += 1
    print(i)
    if i == search_name:
        print(search_name,"present at position :",count)
        print('Stopped the search')
        break
else:
    print("student with name",search_name,"not present")
print("loop has ended")