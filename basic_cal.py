print("Hello World")
a= int(input("Enter first number"))
b= int(input("Enter second number"))
print("select 1 for addition/ 2 for subtraction/ 3 for multiplication/ 4 for division")
operation=int(input("enter choice"))
if operation==1:
    print ("Result is : ", a+b)
elif operation==2:
    print ("Result is : ",(a-b))
elif operation==3:
    print ("Result is : ",(a*b))
elif operation==4:
    print ("Result is : ",(a/b))
else:
    print("Try Again")
