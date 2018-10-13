n=int(input("enter a number"))
factorial=1
if n<0:
   printf("factorial does not exist")
elif n==0:
   printf("factorial of 0 is 1")
else:
for i in range(1,n+1):
  factorial=factorial*i
  printf("factorial is ",factorial)
