def deposit():
    while True:
       amount = input("What would you like to deposit? $ ")
       if amount.isdigit():
           amount = int(amount)
           if amount > 0:
               break
           else:
               print("Amount most be greater than zero")
            else:
                print("Enter a number: ")


    return amount

