
def for_summation(n):
    
    total = 0 
    

    for i in range (1, n + 1):
        total += i 
    return total  



n = int(input("Enter a number : "))
a = for_summation(n)
print(f"the summation of {n} is  {a} ")
