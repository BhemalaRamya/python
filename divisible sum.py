n=int(input("enter a number"))
n1=n
sum=0
while(n>0):
    digit=n%10
    sum=sum+digit
    n=n//10
if(n1%sum==0):
    print("divisible")
else:
    print("not")
    
