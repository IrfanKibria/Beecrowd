given_days = int(input())

day_format = [365, 30, 1]

output = []

for i in day_format:
    var_days = int(given_days/i)
    output.append(var_days)
    reminder = given_days%i
    given_days = reminder

print(f'{output[0]} ano(s)\n{output[1]} mes(es)\n{output[2]} dia(s)')
