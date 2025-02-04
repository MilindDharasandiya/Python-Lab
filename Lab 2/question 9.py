number = float(input("Enter a number: "))
if number < 0:
 number.value = -number
else:
 number.value = number
print( "The absolute value of ",number,"is ",number.value)
