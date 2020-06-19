total_colurs_need=int(input())
each_colour=5.00
canvas_brushes=40.00
cost_total_colurs_need=total_colurs_need*each_colour
total_money_need=canvas_brushes +  cost_total_colurs_need
tax=total_money_need/10
total_money=total_money_need + tax
diff=total_money - int(total_money)
if diff>=0.5:
    print(total_money)
else:
    print(int(total_money))