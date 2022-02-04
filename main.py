from pprint import pprint
sentence = ""
# objective: find most repeated character

print("Counts the frequency of a character")
sentence = input("Enter string: ")
frequency = {}
for char in sentence:
  if char in frequency:
    frequency[char] += 1
  else:
    frequency[char] = 1
# Basically loops once and sets a value of 1 for corrosponding letter, the second time it loops, it adds 1 for every additional letter it finds
sorted_frequency = (sorted(frequency.items(), key=lambda kv:kv[1], reverse=True))
# converts dictionary to tuples | kv = key value pair of 1 which is frequency of each character index 
print(sorted_frequency[1])