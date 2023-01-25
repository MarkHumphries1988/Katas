import math

def digital_root(num):
  if num<=9:
    return num
  else:
    currentpass=0
    while(num>1):
      currentpass+=num%10
      num=math.floor(num/10)
      print(num)
    currentpass+=num
    return digital_root(currentpass)
  pass