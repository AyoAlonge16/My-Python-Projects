num1 = int(input("First number: "))
num2 = int(input("Second number: "))

if num1 == num2:
    print("They are same")
elif num2 >= num1:
    largest = num2
else:
    largest = num1

print("Largest number you entered is:", largest)


