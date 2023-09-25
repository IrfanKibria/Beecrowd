given_amount = int(input())
print(given_amount)

note = [100, 50, 20, 5, 2, 1]

for i in note:
    var_amn = int(given_amount/i)
    print(f'{var_amn} nota(s) de R$ {i},00')

    reminder = given_amount%i
    given_amount = reminder
