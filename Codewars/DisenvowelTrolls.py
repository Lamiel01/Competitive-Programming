# My solution
def disemvowel(string_):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    string_new = ""
    for each in range(len(string_)):
        if str(string_[each]) not in vowels:
            string_new += str(string_[each])
    return string_new
  
# Other solutions
def disemvowel(s):
    return s.translate(None, "aeiouAEIOU")

# 2
def disemvowel(string):
    return "".join(c for c in string if c.lower() not in "aeiou")
