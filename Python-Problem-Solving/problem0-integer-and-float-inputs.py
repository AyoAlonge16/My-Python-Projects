#Problem: Take two inputs from the user, one will be an
#integer and the other will be a float. Then multiply them to display the out put.

#Here is the solution

int_text = input('Give me an integer number: ')
#requesting for a number as input
int_num = int(int_text)

float_text = input('Give me a float  number: ')
#requesting for a float as input
float_num = float(float_text)

result = int_num * float_num

print('Your result is: ', result)


