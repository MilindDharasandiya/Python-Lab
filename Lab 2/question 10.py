length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))
area = length * breadth
perimeter = 2 * (length + breadth)
if area > perimeter:
 print("The area of the rectangle ({area}) is greater than its perimeter ({perimeter}).")
else:
 print("The area of the rectangle ({area}) is not greater than its perimeter ({perimeter}).")
