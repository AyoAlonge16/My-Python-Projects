#in this mini code will request for a value and ask if it can be converted to a number
#pseudo: First we ask for an input, then we print the inputted value. We then move on to check the value with .isdecimal and .isnumeric. then declare that if it is a decimal num should equal int(val) then we print num

value = input("Type in a number: ")
print(value)
print(value.isdecimal())
print(value.isnumeric())

if value.isdecimal():
    num = int(value)
    print(num)
