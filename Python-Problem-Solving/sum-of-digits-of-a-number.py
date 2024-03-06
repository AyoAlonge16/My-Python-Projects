def get_sum_of_digits(num):
   sum = 0
   while(num > 0):
       last_digit = num % 10
       sum = sum + last_digit
       num = num // 10
   return sum
 
user_num=int(input("Enter a number:"))
total = get_sum_of_digits(user_num)
print("The total sum of digits is:",total)


