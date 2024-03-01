

def char_count_while(target, c):
#Implements the character counting using a while loop.
    count = 0 
    i = 0 
    while i < len(target):
        if target[i] == c:
           count += 1
        i += 1
    return count


def char_count_for(target,c):
#Implements the character counting using a for loop\
#(iterating over the string using indices (using range)).

    count = 0 
    for i in range(len(target)):
        if target[i] == c:
            count += 1
    return count


def char_count_foreach(target, c):
#Implements the character counting using a foreach loop\
#(iterating over each character instead of using range).
    count = 0 
    for i in target:
        if i == c:
            count += 1
    return count 

target = "hello"
c = "l"

print(f" the for each produces {char_count_foreach(target, c)} " ) # Expected output: 2
print(f" the while produces {char_count_while(target,c)} ")
print(f" the for produces {char_count_for(target,c)} ") 


