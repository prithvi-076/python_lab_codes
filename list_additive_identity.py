"""
Take a list of length n where all the numbers are non-negative and unique.
Find the element in the list possessing the highest value. Split the
element into two parts where first part contains the next highest value
in the list and second part hold the required additive entity to get the
highest value. 
Print the list where the highest value get splitted into those two parts.

Test case 1:
Enter List Elements:5 3 9 6 2 4
Largest element found at Index 2
New list :[5, 3, 6, 3, 6, 2, 4]
Test case 2:
Enter List Elements:10 5 3 12 
Largest element found at Index 3
New list :[10, 5, 3, 10, 2]
"""
a = list(map(int,input("Enter List Elements:").split()))
i = 0
largest = a[0]
while i < len(a):
  if largest < a[i]:
    largest = a[i]
    largest_index = i
  i += 1
print("Largest element found at Index", largest_index)
sec_largest = a[0]
i = 0
while i < len(a):
  if largest != a[i] and sec_largest < a[i]:
    sec_largest = a[i]
  i += 1
diff = largest - sec_largest
print("New list :",a[:largest_index]+[sec_largest,diff]+a[largest_index+1:])