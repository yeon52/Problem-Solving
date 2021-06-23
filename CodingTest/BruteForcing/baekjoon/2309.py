
dwarf = []

for i in range(9):
    dwarf.append(int(input()))

sum9 = sum(dwarf)
sub = sum9-100
chk = 0
for i in range(9):
    for j in range(i+1, 9):
        a = dwarf[i]
        b = dwarf[j]
        if a+b == sub:
            dwarf.remove(a)
            dwarf.remove(b)
            chk = 1
            break
    if chk == 1:
        break

dwarf.sort()
for i in dwarf:
    print(i)
