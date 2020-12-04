def print_formatted(number):
    for i in range(number):
        decimal = i
        octal = oct(i)
        hexa = hex(i)
        binary = bin(i)
        print(decimal, octal, hexa, binary)


n = 17
print_formatted(n)
