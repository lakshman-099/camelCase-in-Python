from re import sub

# function to convert string to camelCase
def camelCase(string):
  string = sub(r"(_|-)+", " ", string).title().replace(" ", "")
  return string[0].lower() + string[1:]
s1 = input()
s2 = camelCase(s1)
ch=''.join(e for e in s2 if e.isalnum())
print(ch)
