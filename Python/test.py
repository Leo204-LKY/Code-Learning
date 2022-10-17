num = 1
result = 0
while num <= 2019:
  i = str(num)
  if str(2) in i or str(0) in i or str(1) in i or str(9) in i:
    result += num ** 3
  num += 1
print(result)