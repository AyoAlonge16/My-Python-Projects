num1 = int(input("First number: "))
num2 = int(input("Second number: "))
num3 = int(input("Third number: "))

if num1 == num2 == num3:
    print("All three numbers are the same")
else:
    largest = max(num1, num2, num3)
    print("Largest number you entered is:", largest)


