len = int(input("How many numbers do you want to enter? "))
 
nums = []
 
for i in range(0, len):
   element = int(input("Enter element: "))
   nums.append(element)
 
total = sum(nums)
avg = total/len
print("Average of elements you entered",round(avg,2))


