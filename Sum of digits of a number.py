#Sum of digits of a number
n=int(input("Enter any number: "))
sum=0
while(n!=0):
    r=n%10
    sum=sum+r
    n=n//10
print("Sum =",sum)    




#Reverse of a number
n=int(input("Enter any number: "))
sum=0
while(n!=0):
    r=n%10
    sum=sum*10+r
    n=n//10
print("Reverse =",sum)




#Palindrone of a number
n=int(input("Enter any number: "))
s=0
t=n
while(n!=0):
    r=n%10
    s=s*10+r
    n=n//10
print("reverse value is =",s)
if(t==s):
    print("Number is Palindrone")
else:
    print("Number not Palindrone")


#Factorial of a number


n=5
f=1
for i  in range(1,n+1):
    f=f*i
print("Factorial of the number ",n,"is: ",f)



#Prime number

n=int(input("Enter the number="))
f=1
for i in range(2,n):
    if(n%i==0):
        f=0
        break
if(f==1):
    print("Prime number")
else:
    print("Not a Prime Number")
    

