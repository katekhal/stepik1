
up_en = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ' 
en = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz' 
s = input()
k = list(s.split(" "))
f = []
for c in k:
    counter = 0
    for p in c:
        if p.isalpha():
            counter +=1
    for p in c:
        if p.isupper():
            f += up_en[up_en.find(p)+counter%26]
        elif p.islower():
            f += en[en.find(p)+counter%26]
        else:
            f+=p
    print(' ')
print(''.join(f))
