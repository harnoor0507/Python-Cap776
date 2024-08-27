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
