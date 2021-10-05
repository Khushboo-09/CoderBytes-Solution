def LongestWord(sen):

  # code goes here
  x = sen.split(" ")
  l = []
  for i in x:
    if i.isalpha() or i.isnumeric():
      l.append(i)

  if len(l)==1:
    return l[0]
  longest = ''
  for j in range(0,len(l)):
    if len(l[j])==len(longest):
      continue
    elif len(l[j])>len(longest):
      longest = l[j]
  return longest
# keep this function call here 
print(LongestWord(input()))