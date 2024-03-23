def square_sum(num):
    return num * (num + 1) * (2*num + 1) // 6

num = int(input('Enter a number: '))
total = square_sum(num)

print('The sum of square numbers is', total)


