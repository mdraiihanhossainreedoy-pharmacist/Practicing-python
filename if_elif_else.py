#if | elif | else
#problem-1
light = "yellow"
if(light == "green"):
    print("GO")
elif(light == "red"):
    print("STOP")
elif(light == "yellow"):
    print("LOOK")

#problem-2
light = "NO COLOR"
if(light == "green"):
    print("GO")
elif(light == "red"):
    print("STOP")
elif(light == "yellow"):
    print("LOOK")
else:
    print("LIGHT IS ERROR")

#problem-3 | numbers not need " "
marks = 73
if(marks >= 80):
    print("A+")
elif(marks >= 75 and marks < 80):
    print("A")
elif(marks >= 70 and marks < 75):
    print("A-")


#problem-4 | including "int" which make the number valid
marks = int(input("enter students marks : "))
if(marks > 80):
    print("A+")
elif(marks >= 75 and marks < 80):
    print("A")
elif(marks >= 70 and marks < 75):
    print("A-")


#problem-5 | Q. wright a program to find the greatest of 3 numbers entered by the user.
A = int(input("enter first number : "))
B = int(input("enter second number : "))
C = int(input("enter third number : "))
if(A >= B and A >= C):
    print("A is the greatest number")
elif(B >= A and B >= C):
    print("B is the greatest number")
else:
    print("C is the greatest number")


#problem-6 | Q. wright a program to check if a number is a multiple of 7 or not.
X = int(input("enter the number : "))
if(X % 7 == 0):
    print("multiple of 7")
else:
    print("not multiple of 7")


#problem-7 | Q. wright a program to check if a number is even or odd.
Y = int(input("enter the number : "))
if(Y % 2 == 0):
    print("even number")
else:
    print("odd number")