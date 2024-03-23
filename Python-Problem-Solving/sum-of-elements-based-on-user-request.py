def get_sum(nums):
    total_sum = 0
    for num in nums:
        total_sum += num
    return total_sum

# Ask the user for the number of values to sum
num_values = int(input("How many numbers do you want to sum? "))

# Initialize an empty list to store the numbers
nums = []

# Prompt the user to enter each number and add it to the list
for i in range(num_values):
    num = int(input(f"Enter number {i+1}: "))
    nums.append(num)

# Calculate the sum of the numbers
total = get_sum(nums)

# Print the total sum
print("The total sum of the entered numbers is:", total)

