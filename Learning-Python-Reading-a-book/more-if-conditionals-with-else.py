#in this code I will verify the value of the denominator that will be dividing the value of a

def main():
    a = input("Input the first number: ")
    b = input("Input the second nummber: ")
    
    if int(b) == 0:
        print("Division by Zero is ERROR")
    else:
        print("Dividing", a , "by", b)
        print(int(a) / int(b))

main()
    
