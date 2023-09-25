in_time = int(input())

sec = [3600, 60, 1]
ans = []

for i in sec:
    var_time = int(in_time/i)
    ans.append(var_time)
    reminder = in_time%i
    in_time = reminder
    
print(f'{ans[0]}:{ans[1]}:{ans[2]}')