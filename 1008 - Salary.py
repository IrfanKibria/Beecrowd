
emp_no = int(input())
amn_per_hr = int(input())
work_hour = float(input())


sal = float(amn_per_hr * work_hour)

print("NUMBER = %d" %emp_no)
print("SALARY = U$%0.2f" %sal)



emp_no = int(input())
amn_per_hr = int(input())
work_hour = float(input())


sal = float(amn_per_hr * work_hour)

print(f"Number = {emp_no}\nSALARY = U$ {sal:0.2f}")