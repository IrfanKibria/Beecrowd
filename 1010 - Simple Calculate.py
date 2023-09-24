code, unit, price = input().split()
code1, unit1, price1 = input().split()


amn = float(int(unit)*float(price))

amn1 = float(int(unit1)*float(price1))
total = float(amn +amn1)


print(f"VALOR A PAGAR: R$ {total:0.2f}")



product = input().split()
product1 = input().split()

code, unit, price = product
code1, unit1, price1 = product1

amn = float(int(unit)*float(price))

amn1 = float(int(unit1)*float(price1))
total = float(amn +amn1)


print(f"VALOR A PAGAR: R$ {total:0.2f}")