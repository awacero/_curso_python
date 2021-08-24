

def calculate_fibonacci(n):
    
    n1,n2 = 0,1
    count = 1
    if n<0:
        print("Numeros mayores que cero")
    elif n==0:
        print(0)
    elif n==1:
        print(0,1)
    else:
        while count < n:
            print(n1)
            nth = n1 + n2
            n1=n2
            n2=nth
            count +=1


def fibo(n):
    a,b = 0,1

    while a < n:
        print(a, end=' ')
        a,b = b, a+b
    #print()



