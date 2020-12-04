A=input()
def reverse(A):
    string=""
    for i in A:
       string=i + string
    return string
print(reverse(A))