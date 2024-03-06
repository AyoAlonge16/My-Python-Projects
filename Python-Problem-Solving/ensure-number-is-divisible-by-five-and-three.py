def divisible_by_3and5(num):
   result = [ ]
   for i in range(num):
       if i%3 == 0 and i%5 == 0:
           result.append(i)
   return result
 
num = int (input('Enter your number: '))
result = divisible_by_3and5(num)
print(result)

