iiom __future__ import print_function


'''
def main():
    print("Hello World")

if __name__ == "__main__":
    main()
'''

'''
def main():
	print("We have a question for you!")
	name = input('Your name: ')
	print('Hello ' + name + ', how are you?')
main()
'''

#A code that works for both python 3 and python 2


import sys

def main():
    if sys.version_info.major < 3:
        name = raw_input('Your name: ')
    else:
        name = input('Your name: ')
    print('Hello ' + name + ', how are you?')
    
main()


