num=int(input("enter the number"))
factorial=1
if num<0:
  print("factorial of 0 does not exist")
if num==0:
  print("factorial of 0 is 1")
if num>1:
  for i in range(1,num+1):
    factorial=factorial*i
print("the factorial of the given number is",factorial)
