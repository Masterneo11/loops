
def reverse_while(s):
    b = []
    i = 0 
    while i < len(s):
        b.append(s[i])
        i += 1
    b = b[::-1]
    bstr = ''.join(b)
    return bstr

def reverse_for(s):
    reverse_list = []
    for i in range(len(s)):
        reverse_list.append(s[i])
    reverse_list = reverse_list[::-1]
    reverse_string = ''.join(reverse_list)
    return reverse_string



def reverse_foreach(s):
    reverse_list = []
    for i in s:
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