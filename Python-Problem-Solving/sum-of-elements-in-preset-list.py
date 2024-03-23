
def get_sum(nums):
   sum = 0
   for num in nums:
       sum = sum + num
   return sum


nums = [13,89,65,42,12,11,56]

total = get_sum(nums)
print("The total of each elements:",total)


