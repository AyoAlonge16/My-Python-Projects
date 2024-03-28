#this code will help us to compare the greater number between the two inputs

def main():
    a = input("Input the first number here: ")
    b = input("Input the second number here: ")

    if a == b:
        print("Both numbers are equal!")
    else:
        if int(a) > int(b):
            print(a + " is bigger than " + b)
        else:
            print(a + " is less than " + b)

main()
