#Assignment-2
#w.a.p weather the given number is armstrong or not
s=0;
n = int(input("Enter a number: "))
temp=n;
while temp>0:
    a=temp%10
    s+=a**3
    temp //= 10

if n==s:
    print(n,"is an Armstrong number")

else:
    print(n,"is not an Armstrong number")
