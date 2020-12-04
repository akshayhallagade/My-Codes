import math as m
raw_input = int(input())
toothbrush = 1
dollar_bills = 2
candy = raw_input-(toothbrush+dollar_bills)

if raw_input == 3:
    print(m.ceil(dollar_bills*100/raw_input))
elif raw_input >= 3:
    print(m.ceil(dollar_bills*100/raw_input))
