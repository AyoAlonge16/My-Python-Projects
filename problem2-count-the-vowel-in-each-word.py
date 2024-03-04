def count_vowels(sentence):
  count = 0
  vowels = ['a','e','i','o','u','A','E','I','O','U']
  for char in sentence:
     if char in vowels:
        count += 1
  return count

sentence = input("Type in your word or sentence: ")
print(count_vowels(sentence))




