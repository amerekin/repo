# HW1
seconds = int(input('Enter duration in sec: '))

if seconds >= 86400:
    days = seconds // 86400
    hours = seconds % 86400 // 3600
    minutes = seconds % 86400 % 3600 // 60
    seconds = seconds % 86400 % 3600 % 60
    print(days, 'days,', hours, 'hours,', minutes, 'min and', seconds, 'sec')

elif seconds >= 3600:
    hours = seconds // 3600
    minutes = seconds % 3600 // 60
    seconds = seconds % 3600 % 60
    print(hours, 'hours,', minutes, 'min and', seconds, 'sec')

elif seconds >= 60:
    minutes = seconds // 60
    seconds = seconds % 60
    print(minutes, 'min and', seconds, 'sec')

else:
    print(seconds, 'сек')
