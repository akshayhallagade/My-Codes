print("spam"*3)
# spamspamspam

print(4*'2')
# 2222

print('17' * '87')
# Error:
# Traceback (most recent call last):
#  print('17' * '87')
# TypeError: can't multiply sequence by non-int of type 'str'

print('pythonisfun'*7.0)
# Error:
# Traceback (most recent call last):
# print('pythonisfun'*7.0)
# TypeError: can't multiply sequence by non-int of type 'float'
