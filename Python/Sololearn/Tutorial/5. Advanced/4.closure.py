def make_nultiplier_of(n):
    def multiplier(x):
        return x*n
    return multiplier

times3=make_nultiplier_of(3)
times5=make_nultiplier_of(5)

print(times3(9))
print(times5(3))
print(times5(times3(2)))