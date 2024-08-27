#Sum of digits of a number
n=int(input("Enter any number: "))
sum=0
while(n!=0):
    r=n%10
    sum=sum+r
    n=n//10
print("Sum =",sum)    
