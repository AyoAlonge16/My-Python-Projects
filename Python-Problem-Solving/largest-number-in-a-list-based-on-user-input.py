def get_largest(nums):
    largest = nums[0]
    for i, num in enumerate(nums, start=1):
        if num > largest:
            largest = num
    return largest

# Ask the user for the number of values to compare
num_values = int(input("How many numbers do you want to compare? "))

# Initialize an empty list to store the numbers
nums = []

# Prompt the user to enter each number and add it to the list
for i in range(num_values):
    num = int(input(f"Enter number {i+1}: "))
    nums.append(num)

# Find the largest number
largest = get_largest(nums)

# Print the largest number
print('The largest number is:', largest)


