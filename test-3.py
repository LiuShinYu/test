n = int(input('人數:'))
num = []
for a in range(n):
    num.append(a + 1)

a = 0     
b = 0   
c = 0     

while c < n - 1:
    if num[a] != 0:
        b += 1
    if b == 3:
        num[a] = 0
        b = 0
        c += 1
    a += 1
    if a == n:
        a = 0

a = 0
while num[a] == 0:
    a += 1
print(num[a])