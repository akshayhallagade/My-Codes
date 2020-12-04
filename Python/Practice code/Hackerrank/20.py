def birthdayCakeCandles(candles):
    maxx = max(candles)
    cout = 0
    for i in candles:
        if maxx == i:
            cout += 1
    print(cout)


birthdayCakeCandles([3, 2, 1, 3])
