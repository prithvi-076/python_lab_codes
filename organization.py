'''
An organization Speed Technology recruited some new employees whose ids
Starts from 565892.

The Company segregates the employees into TechVision & CodeBrigade teams based on following conditions:
If the employeeID is
i. Display the list of employee Ids
ii.Divisible by 2&3 then ---TechVision Team
iii.Otherwise ---CodeBrigade Team
Display the List of employeeID’s of Tech Vision Team & Code Bridge Team
case 1:
Enter no of Employees joined:10
Employee nos: [565892, 565893, 565894, 565895, 565896, 565897, 565898, 565899, 565900, 565901]
Team TechVision : [565896]
Team CodeBrigade : [565892, 565893, 565894, 565895, 565897, 565898, 565899, 565900, 565901]
case 2:
Enter no of Employees joined:22
Employee nos: [565892, 565893, 565894, 565895, 565896, 565897, 565898, 565899, 565900, 565901, 565902, 565903, 565904, 565905, 565906, 565907, 565908, 565909, 565910, 565911, 565912, 565913]
Team TechVision : [565896, 565902, 565908]
Team CodeBrigade : [565892, 565893, 565894, 565895, 565897, 565898, 565899, 565900, 565901, 565903, 565904, 565905, 565906, 565907, 565909, 565910, 565911, 565912, 565913]
'''
n = int(input("Enter no of Employees joined:"))
list1 = []
x = 565892
for i in range(n):
    list1.append(x)
    x += 1
print("Employee nos:",list1)
TechVision=[]
CodeBrigade=[]
for i in list1:
    if i%2==0 and i%3==0:
        TechVision.append(i)
    else:
        CodeBrigade.append(i)
print("Team TechVision :",TechVision)
print("Team CodeBrigade :",CodeBrigade)
