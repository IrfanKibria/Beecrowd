name = input()
sal = float(input())
sell = float(input())


com = float((sell*15)/100)

total_sal = float(sal +com)

print (f"TOTAL = R$ {total_sal:0.2f}")