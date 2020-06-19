#replacing the strng within the line.
A="akshay"
S="Ash"
Last="This is a {} and this is his gf {}".format(A,S)
Last2="This is a {1} and this is his gf {0}".format(A,S) #exchanging
Last3=f"This is a {S} and this is his gf {A}"#3.6 onwards new feature.
print(Last)
print(Last2)
print(Last3)