# sum of last U digits
n=int(input())
u_digit=n%10
total=0
for i in range (-1,u_digit-1):
    temp=n%10
    n=n//10
    total+=temp
print(total)
