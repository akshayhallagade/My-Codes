cities = {"malaysia": 0, "Australia": 0, "Germany": 0, "Dubai": 0, "France": 0}
for i in range(5):
    for j in cities:
        a = int(input())
        cities[j] += a
print(cities)
