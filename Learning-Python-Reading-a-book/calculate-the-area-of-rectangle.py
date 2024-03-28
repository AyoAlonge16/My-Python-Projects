#QUESTION: Write a script that will ask for the sides of a rectangule and print out the area
#Provide error messages if the either of the sides is negative

def main():
    length = int(input("What is the length of the RECTANGLE: "))
    breadth = int(input("What is the breadth of the RECTANGLE: "))
    
    if length <= 0 or breadth <= 0:
        print("Input the right values")
        return

    area = length * breadth
    print("The area of the RECTANGLE is ", area)

main()
