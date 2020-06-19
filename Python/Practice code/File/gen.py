def make_word():
    word=""
    for ch in "Akshay":
        word +=ch
        yield word
print(list(make_word()))        