a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))
if a >= b and a >= c:
 largest = a
elif b >= a and b >= c:
 largest = b
else:
 largest = c
if a <= b and a <= c:
 smallest = a
elif b <= a and b <= c:
 smallest = b
else:
    smallest = c
print("Largest number: ",largest)
print("Smallest number: ",smallest)
