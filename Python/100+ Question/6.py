from math import isqrt
D = (100, 150, 180)
D = list(D)
C = 50.0
H = 30.0
Q_list = []
for i in D:
    Q = isqrt(int((2*C*i)/H))
    Q_list.append(Q)
print(Q_list)
