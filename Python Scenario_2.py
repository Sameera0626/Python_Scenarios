a = [1, 2, 5, 3, 4]
b = [8, 7, 9, 5]
c = [4, 2, 1, 5]

# Convert the lists to sets for efficient intersection
common = set(a).intersection(b, c)

# Convert the set back to a list
common_list = list(common)

print("Common elements:", common_list)

Task 2:
Take common letter out

i = "JEVSACEA"

#initialize a empty dictionary to store character counts

char_counts={}

#count each character's occurences
for char in i:
  if char in char_counts:
    char_counts[char] +=1

else:
  char_counts[char] = 1


#find charcaters that appear more than once
common_letters=[char in char, count in char_counts.items() if count >1]

print("common words:",common_letters)

