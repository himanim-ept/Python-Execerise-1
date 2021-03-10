#Write a Python program to count the number of strings in a list
# where the string length is 2 or more
# and the first and last character are the same from a given list of strings.


list1  = ["himani","maheta","aba"]
def match_words(list1):
  ctr = 0

  for word in list1:
    if len(word) > 1 and word[0] == word[-1]: # check the string length and the first and last char is same
      ctr += 1
  return ctr

print(match_words(list1))
