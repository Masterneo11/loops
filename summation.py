

def summation(n):
    total = 0 
    i = 1

    while i <= n:
        total += i 
        i += 1 

    return total 


n = int(input("enter a number : "))
a = summation(n)
print(a)
