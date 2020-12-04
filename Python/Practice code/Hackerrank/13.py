height, width = 7, 21
"""list(map(int, input().split(" ")))"""

for j in range(1, height-1, 2):
    txt = ".|."*j
    print(txt.center(width, "-"))
print("WELCOME".center(width, "-"))
for j in range(height-2, 0, -2):
    txt = ".|."*j
    print(txt.center(width, "-"))
