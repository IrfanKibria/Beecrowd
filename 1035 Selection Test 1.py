a,b,c,d = map(int, input().split())

if b>c & d>a & ((c+d)>(a+b)) & c>= 0 & d>= 0 & a%2==0:
    print("Valores aceitos")

else:
    print("Valores nao aceitos")




A, B, C, D = map(int, input().split())

if ( B>C and  D>A and (C+D) > (A+B) and C>0 and D>0 and A%2==0):
    print ('Valores aceitos')

else:
    print('Valores nao aceitos')
