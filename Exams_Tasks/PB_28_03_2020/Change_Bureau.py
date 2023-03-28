bitcoins = int(input())
ch_uan = float(input())
commission = float(input())
dollars = ch_uan * 0.15
total = (bitcoins * 1168) + (dollars * 1.76)
euro = total / 1.95
euro = euro * 0.95
print(f"{euro:.2f}")
