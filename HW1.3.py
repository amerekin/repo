
proc_list = []

for i in range(100):
    proc_list.append(i + 1)

for j in proc_list:
    if 9 < j < 20:
        print(j, 'процентов')
    elif j % 10 == 1:
        print(j, 'процент')
    elif 1 < j % 10 < 5:
        print(j, 'процента')
    else:
        print(j, 'процентов')
