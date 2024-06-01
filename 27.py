a=float(input("enter value of a:"))
b=float(input("enter value of b:"))
c=float(input("enter value of c:"))
d=float(input("enter value of d:"))
if c-d!=0:
    result = (a+b)/(c-d)
    print("the result of(a+b)/(c-d) is:",result)
else:
    print("division by zero is not allowed")