def main():
    import ESSENTIAL_FUNCTIONS
    import time
    from datetime import datetime
    print("Good Morning, Welcome to Class! Please Sign in!")
    student_login = ESSENTIAL_FUNCTIONS.input_name()
    while True:
        clock_in = input("Are you ready to clock in. If so type (clock-in): ")
        if clock_in == "clock-in":
            break
        else:
            print("Type clock-in please!")
    print('You have clocked in   :', datetime.now())
    your_data = {"Purchase Amount": 'TotalAmount'}
    with open('LOGINTIMES.txt', 'a') as f:
        f.write('\n')
        f.write(student_login) 
        f.write('\n')
        f.write('\n Clocked In at ') 
        f.write(datetime.now())
        f.write('\n')
    restart = input("Type next to allow the next student to clock in: ").lower()
    if restart == "next":
        main()
    else:
        exit()

main()

