#Assignment-3
#w.a.p to get factorial numbers upto n series.
s=1;
def factorial_of_number(n):
    global s;
    if n>0:
        s=s*n;
        factorial_of_number(n-1)
    else:
        print(s)
        s=1;


#test cases
factorial_of_number(2)
factorial_of_number(3)
factorial_of_number(4)
factorial_of_number(5)
