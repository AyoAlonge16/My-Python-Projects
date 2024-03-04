while True:
    try:
        num_fibonacci = int(input("How many Fibonacci numbers would you like to generate? "))
        break  # Exit the loop if input is successfully converted to an integer
    except ValueError:
        print("Invalid input. Please enter an integer.")

fibonacci_sequence = [0, 1]  # Initial sequence with first two Fibonacci numbers

# Generate Fibonacci numbers
for _ in range(2, num_fibonacci):
    next_fibonacci = fibonacci_sequence[-1] + fibonacci_sequence[-2]
    fibonacci_sequence.append(next_fibonacci)

# Display the generated Fibonacci sequence
print("The Fibonacci sequence with", num_fibonacci, "numbers is:")
print(fibonacci_sequence)


