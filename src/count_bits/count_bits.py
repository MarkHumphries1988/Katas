def count_bits(integer):
  binary=str(bin(integer))
  count=0
  for digit in binary:
    if digit=="1":
      count+=1

  return count
  


  pass