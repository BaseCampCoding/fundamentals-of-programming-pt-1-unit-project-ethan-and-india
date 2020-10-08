def main():
    import ESSENTIAL_FUNCTIONS
    from datetime import datetime
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%d-%b-%Y (%H:%M:%S.%f)") 
    print("Good Morning, Welcome to Class! Please Sign in!")
    student_login = ESSENTIAL_FUNCTIONS.input_name()
    while True:
        clock_in = input("Are you ready to clock in. If so type (clock-in): ")
        if clock_in == "clock-in":
            break
        else:
            print("Type clock-in please!")
    print('You have clocked in   :',  timestampStr )
 
    dateTimeObj = datetime.now()
    current_time = dateTimeObj.strftime("%H:%M:%S")
    start = 80000
    end = 81520
    current_time = str.replace(current_time, ':', '')
    current_time = int(current_time)
    if current_time > start and current_time > end:
        print("It's past 8:15 A.M YOU ARE LATE!")
           
           
    with open('LOGINTIMES.txt', 'a') as f:
        f.write('\n')
        f.write(student_login) 
        f.write('\n')
        f.write('\n Clocked In at ') 
        f.write( timestampStr)
        f.write('\n')
    restart = input("Type next to allow the next student to clock in: ").lower()
    if restart == "next":
        main()
    else:
        exit()

main()

