def fibonacci(num):
    fibo = [0, 1]
    i = 2
    while i <= num:
        next_fibo = fibo[i - 1] + fibo[i - 2]
        fibo.append(next_fibo)
        i += 1
    return fibo

num_fibonacci = int(input("How many Fibonacci numbers would you like to generate? "))
print(fibonacci(num_fibonacci))




