a=int(input("enter the number"))
if a>1:
 for i in range(2,a):
    if (a%i)==0:
      print("the number is not prime")
      print(i,"times",a//i,"is",a)
      break
 else:
    print("the number is prime")

