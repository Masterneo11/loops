 

def list_multiply_while(a: list[int], b : list[int]) -> list[int]:
    # Implements the multiplication using a while loop.

    total = []
    i = 0 
    while i < len(a):
      c = a[i] * b[i]
      total.append(c)
      i += 1
         
    return total 
        
def list_multiply_for(a: list[int], b: list[int]) -> list[int]:
    # in here implement a for loop \
    #Implements the multiplication \
    #using a for loop (iterating over the items in the lists\
    #using indices (using range)).
   
    total = []
    #for i in range(len(a)):
        #for i in range(len(b)):
    for i in range(len(a)):
              c = a[i] * b[i]
              total.append(c)
              
    return total

# example 
a = [1, 2, 3]
b = [4, 5, 6]
print(f"for in range {list_multiply_for(a,b)} ")
print("")

print(f" while loop {list_multiply_while(a,b)} ")
  # This should compute [1*4, 2*5, 3*6]
  # Expected output: [4, 10, 18]
