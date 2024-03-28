def main():
    a = input("Insert your first value: ")
    b = input("Insert your second value: ")

    if a == b:
        print("Both are equal")
    elif int(a) < int(b):
        print(a + " is smaller than " + b)
    else:
        print(a + " is greater than " + b)
        
main()

