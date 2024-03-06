num1 = int(input("First number: "))
num2 = int(input("Second number: "))
num3 = int(input("Third number: "))
 
largest = num1
 
if (num2 >= num1) and (num2 >= num3):
   largest = num2
elif (num3 >= num1) and (num3 >= num2):
   largest = num3
else:
   largest = num1
 
print("Largest number you entered is: ",largest)


