n=int(input())
a=n
x=0
while n>0:
    rem=n%10
    n=n//10
    x+=rem
print(x)
if a%x==0:
    print(a,'is a harsh number')
else:
    print(a,'is not a harsh number')
