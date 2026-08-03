def odd_even(n):
    if n % 2 == 0:
        return 'EVEN'
    else:
        return 'ODD'

def prime(n):
    if n < 0:
        return "NEGATIVE"
    elif n == 0:
        return "ZERO"
    elif n == 1:
        return "NEITHER PRIME NOR COMPOSITE"
    for i in range(2, n):
        if n % i == 0:
            return "NOT PRIME"
    return "PRIME"

def sum(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum
def sum_series(n,i=1):
    if i < n:
        print(i,end=' + ')
        sum_series(n,i+1)
    elif i == n:
        print(f"{n} = {sum(n)}")
    else:
        return

def fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact
def fact_series(n,i=1):
    if i < n:
        print(i,end=' x ')
        fact_series(n,i+1)
    elif i == n:
        print(f"{n} = {fact(n)}")
    else:
        return
    
n = int(input('Enter a number: '))
print(f"\nThe Number {n} is: {odd_even(n)} and {prime(n)}")
sum_series(n)
fact_series(n)
