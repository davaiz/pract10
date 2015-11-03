libr = open('en-ru.txt', 'r')
input = open('input.txt', 'r')
output = open('output.txt', 'w')
libline = libr.readlines()
lib = dict()
for i in libline:
    k = i.split('	-	')
    lib[k[0]] = k[1] 
inline = input.readline()
inline = inline.split()
for q in inline:
    q = A[q]
print(' '.join(inline))  





    
    
