x = float(input("Enter the x-coordinate of the circle's centre: "))
y = float(input("Enter the y-coordinate of the circle's centre: "))
r = float(input("Enter the radius of the circle: "))
px = float(input("Enter the x-coordinate of the point: "))
py = float(input("Enter the y-coordinate of the point: "))
distance.squared = (px - x) ** 2 + (py - y) ** 2
radius.squared = r ** 2
if distance.squared < radius.squared:
 print("The point lies inside the circle.")
elif distance.squared == radius.squared:
 print("The point lies on the circle.")
else:
     print("The point lies outside the circle.")
