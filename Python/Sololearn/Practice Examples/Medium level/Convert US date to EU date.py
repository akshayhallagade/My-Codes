df = "01/31/2014"
# f = []
# for a in df:
s = list(df)
d = "{3}{4}{2}{0}{1}{5}{6}{7}{8}{9}".format(
    s[0], s[1], s[2], s[3], s[4], s[5], s[6], s[7], s[8], s[9]
)
# f.append("".join(d))
print(d)
