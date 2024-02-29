

def reverse_while(s):
    # implements the reversing using a while loop
    b = []
    i = 0 

    while i < len(s):

        b.append(s[i])
        i += 1
    b = b[::-1]
    bstr = ' '.join(b)
    return bstr

def reverse_for(s):
    # implements the reversing using a for loop(iterating over \
    # the actual string indices(using range))
    reverse_list = []

    #for i in range(5):
    for i in range(len(s)):
        
        reverse_list.append(s[i])
    reverse_list = reverse_list[::-1]
    reverse_string = '-'.join(reverse_list)
    return reverse_string  



def reverse_foreach(s):
    # implements the reversing using a foreach loop.Iterating \
    # over the actual characters in the string, not using range

    reverse_list = []
    for i in s:
       # s[-1]
         reverse_list.append(i)
    reverse_list = reverse_list[:: -1]
    reverse_string = ''.join(reverse_list)
    return reverse_string


#Example:
s = "hello"
print(reverse_for(s))
print(reverse_while(s))
print(reverse_foreach(s))

#print(r) # Expected output: "olleh"
