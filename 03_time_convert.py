dash = "-----------------------------------------" 

def hour_min():
    hour = int(input("Enter time in hours: "))
    min = 60*hour
    print(f"{dash}\n{hour} hours is: {min} minutes.\n{dash}")

def min_sec():
    min = int(input("Enter time in minutes: "))
    sec = 60*min
    print(f"{dash}\n{min} minutes is: {sec} seconds.\n{dash}")

def hour_sec():
    hour = int(input("Enter time in hours: "))
    sec = 3600*hour
    print(f"{dash}\n{hour} hours is: {sec} seconds.\n{dash}")

def sec_min():
    sec = int(input("Enter time in seconds: "))
    min = sec // 60
    sec_ = sec % 60
    print(f"{dash}\n{sec} seconds is: {min} minutes and {sec_} seconds.\n{dash}")

def min_hour():
    min = int(input("Enter time in minutes: "))
    hour = min // 60
    min_ = min % 60
    print(f"{dash}\n{min} minutes is: {hour} hours and {min_} minutes.\n{dash}")

def sec_hour():
    sec = int(input("Enter time in seconds: "))
    hour = sec // 3600
    rem = sec % 3600
    min = rem // 60
    sec_ = rem % 60
    print(f"{dash}\n{sec} seconds is: {hour} hours, {min} minutes and {sec_} seconds.\n{dash}")

# hour_min()       #[ Calling of functions ]
# min_sec()
# hour_sec()
# sec_min()
# min_hour()
# sec_hour()