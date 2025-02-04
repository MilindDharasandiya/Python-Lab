subject1 = int(input("Enter marks for Subject 1: "))
subject2 = int(input("Enter marks for Subject 2: "))
subject3 = int(input("Enter marks for Subject 3: "))
pass status = True
if subject1 <= 39 or subject2 <= 39 or subject3 <= 39:
    pass status = False
total marks = subject1 + subject2 + subject3
average marks = total marks / 3
if subject1 >= 90:
 grade1 = "A"
elif subject1 >= 75:
 grade1 = "B"
elif subject1 >= 50:
 grade1 = "C"
elif subject1 >= 40:
 grade1 = "D"
else:
 grade1 = "Fail"
if subject2 >= 90:
 grade2 = "A"
elif subject2 >= 75:
 grade2 = "B"
elif subject2 >= 50:
 grade2 = "C"
elif subject2 >= 40:
 grade2 = "D"
else:
 grade2 = "Fail"
if subject3 >= 90:
 grade3 = "A"
elif subject3 >= 75:
 grade3 = "B"
elif subject3 >= 50:
 grade3 = "C"
elif subject3 >= 40:
 grade3 = "D"
else:
 grade3 = "Fail"
print("\n Results:")
print( "Total Marks: {total marks}")
print( "Average Marks: {average_marks:.2f}")
if pass status:
 print("Status: Pass")
else:
 print("Status: Fail")
print( "Grade in Subject 1: {grade1}")
print("Grade in Subject 2: {grade2}")
print( "Grade in Subject 3: {grade3}")
