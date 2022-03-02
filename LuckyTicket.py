nomer = int(input())

r = nomer % 1000
a = r % 10
a1 = r // 10
b = a1 % 10
b1 = a1 // 10
c = b1 % 10
resultR = a + b + c

l = nomer // 1000
d = l % 10
d1 = l // 10
e = d1 % 10
e1 = d1 // 10
f = e1 % 10
resultL = f + e + d
if resultL == resultR:
    print("Счастливый")
else:
    print("Обычный")