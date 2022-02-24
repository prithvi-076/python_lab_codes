"""
Aswith is having three buildings A, B, C. Every month he gets of rents from A, B, C.
Also, he gets salary. 
Based on his total monthly income, he spends the amount to 
Orphanage, family, other expenses as following:
If  income <50000 spends 15% to Orphanage, 30% to family, 10% to other Expenses
If income >=50000 & income <100000 spends 20% to Orphanage, 30% to family, 15% to other Expenses
If income >=100000 spends 20% to Orphanage, 35% to family, 15% to other Expenses
Calculate the savings of Aswith in a month and display.
case=1
Enter building 1 rent :5000
Enter building 2 rent :7500
Enter building 3 rent :9000
Enter salary :16000
Total amount : 37500
savings : 16875
case=2
Enter building 1 rent :15000
Enter building 2 rent :12000
Enter building 3 rent :22000
Enter salary :30000
Total amount : 79000
savings : 27650
case=3
Enter building 1 rent :30000
Enter building 2 rent :32000
Enter building 3 rent :45000
Enter salary :35000
Total amount : 142000
savings : 42600
"""
b1=int(input("Enter building 1 rent :"))
b2=int(input("Enter building 2 rent :"))
b3=int(input("Enter building 3 rent :"))
s=int(input("Enter salary :"))
total=b1+b2+b3+s
print("Total amount :",total)
if total<50000:
    orp=total*0.15
    fam=total*0.30
    oth=total*0.10
    exp=orp+fam+oth
    print("savings :",int(total-exp))
elif total>=50000 and total<100000:
    orp=total*0.20
    fam=total*0.30
    oth=total*0.15
    exp=orp+fam+oth
    print("savings :",int(total-exp))
elif total>=100000:
    orp=total*0.20
    fam=total*0.35
    oth=total*0.15
    exp=orp+fam+oth
    print("savings :",int(total-exp))
