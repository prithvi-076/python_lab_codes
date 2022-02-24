"""
A professor calls out studentIDs of students one by one while marking attendance.
He notices that the number of students recorded in the attendance sheet is far 
more than the number of students who are actually present in the classes.
Hence, he decides to use a chitti the robot which can record the students' 
voices and keep track of which students have responded to attendance calls.
At the end of each session, the robot outputs the student IDs of the students
who have responded to attendance calls. With this information,
the professor needs your help to find out which students were absent.
Write a program which takes an integer array a denoting the student IDs recorded
by the robot and print the list of student IDs of the students which
were absent in increasing order.

Sample input&Output:
Enter strength of class: 8                                                                                              
Enter attendance: 8 7 5 6 8 2 4 3
List of student IDs of the students which were absent:                                                                  
1                                                                                                                       
  
Enter strength of class: 6   
Enter attendance: 7 8 5 7 2 1 3 4 
List of student IDs of the students which were absent:
6
"""
st = int(input("Enter strength of class: "))
att = list(map(int, input("Enter attendance: ").split()))
absent = []
for i in range(1, st + 1):
    if i not in att:
        absent.append(i)
print(f"List of student IDs of the students which were absent:\n{absent}")