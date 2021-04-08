def sum():
    x=int(input("enter 1st number here:"))
    y=int(input("enter 2nd number here:"))
    z=x+y
    print(z)
def sub():
    a=int(input("enter 1st number here:")) 
    b=int(input("enter 2nd number here:"))
    p=a-b 
    print(p)  
def multi():
    c=int(input("enter 1st number here:"))
    d=int(input("enter 2nd number here:"))
    s=c*d
    print(s) 
def div():
    e=int(input("enter 1st number here:")) 
    f=int(input("enter 2nd number here:")) 
    h=e/f
    print(h)  
print("welcome to calculator")
print('''what do you want to do
1>add
2>minus
3>divide
4>multiplication
options = 1,2,3,4''')
uda=int(input(":"))
if uda==1 :
    sum()
elif uda==2:
    sub()
elif uda==3:
    div()  
elif uda==4 :
    multi()      
else:
    print("error")    