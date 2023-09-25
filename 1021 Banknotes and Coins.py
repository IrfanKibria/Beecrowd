amount = float(input())

notes = [100, 50, 20, 10, 5, 2]
coins = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print('NOTAS:')

for i in notes:
    var_amount = int(amount/i)
    print(f'{var_amount} nota(s) de R$ {i:0.2f}')
    reminder = amount%i
    amount = reminder
    
print('MOEDAS')


for j in coins:
    var_amount = int(round(amount,2)/j)
    print (f'{var_amount} moeda(s) de R$ {j:0.2f}')
    reminder = amount%j
    amount = reminder

