text = input("Type in your sentence: ")
count = 0
for char in text:
   if char == ' ':
       count = count + 1
#add one for the last word
count = count + 1

print(count)


