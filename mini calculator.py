x=int(input("enter the number"))
y=int(input("enter the number"))
o=input("enter the operator")
add=x+y
sub=x-y
multiply=x*y
divide=x/y
if o=="+":
    print(add)
elif o=="-":
    print(sub)
elif o=="*":
    print(multiply)
elif o=="/":
    print(divide)
else:
    print("invalid")
