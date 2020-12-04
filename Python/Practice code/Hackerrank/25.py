def minion_game(st):
    a = ["A", "E", "I", "O", "U"]
    cout_Kevin, cout_Stuart = 0, 0
    # for kevin
    for i in range(len(st)):
        for j in range(len(st)):
            try:
                cut = (st[i:j+i])
                if cut[0] not in a:
                    cout_Kevin += st.count(cut)
                else:
                    cout_Stuart += st.count(cut)
    if cout_Stuart > cout_Kevin:
        print("Stuart", str(cout_Stuart))
    elif cout_Kevin > cout_Stuart:
        print("Kevin", str(cout_Kevin))


minion_game("BANANA")
