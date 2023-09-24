'''
a = float(input())
b = float(input())
c = float(input())


tri = float(0.5 * a*c)

circle = float(3.14159 * c**2)

trap = float((a+b)/2*c)

squ = float(b**2)

rec = float(a*b)


print(f"TRIANGULO: {tri:0.3f}")

print(f"CIRCULO: {circle:0.3f}")

print(f"TRAPEZIO: {trap:0.3f}")

print(f"QUADRADO: {squ:0.3f}")

print(f"RETANGULO: {rec:0.3f}")
'''


'''
ls = map(float, input().split())

a,b,c = ls


tri = float(0.5 * a*c)

circle = float(3.14159 * c**2)

trap = float((a+b)/2*c)

squ = float(b**2)

rec = float(a*b)


print(f"TRIANGULO: {tri:0.3f}")

print(f"CIRCULO: {circle:0.3f}")

print(f"TRAPEZIO: {trap:0.3f}")

print(f"QUADRADO: {squ:0.3f}")

print(f"RETANGULO: {rec:0.3f}")
'''



a,b,c = map(float, input().split())

tri = float(0.5 * a*c)

circle = float(3.14159 * c**2)

trap = float((a+b)/2*c)

squ = float(b**2)

rec = float(a*b)


print(f"TRIANGULO: {tri:0.3f}\nCIRCULO: {circle:0.3f}\nTRAPEZIO: {trap:0.3f}\nQUADRADO: {squ:0.3f}\nRETANGULO: {rec:0.3f}")


