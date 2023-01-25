def alphabet_position(string):
  if(len(string)==0):
    return string
  returnstr=[]
  for c in string.lower():
    if 97<=ord(c)<=122:
      returnstr.append(str(ord(c)-96))

  return " ".join(returnstr)

  pass