def main():
    import ESSENTIAL_FUNCTIONS
    import time
    print("Good Morning, Welcome to Class! Please Sign in!")
    x = ESSENTIAL_FUNCTIONS.input_name()
    while True:
        clock_in = input("Are you ready to clock in. If so type (clock-in): ")
        if clock_in == "clock-in":
            break
        else:
            print("Type clock-in please!")
    print('You have clocked in   :', time.ctime())
    your_data = {"Purchase Amount": 'TotalAmount'}
    with open('LOGINTIMES.txt', 'a') as f:
        f.write('\n')
        f.write(x ) 
        f.write('\n')
        f.write('\n Clocked In at ') 
        f.write(time.ctime())
        f.write('\n')
    restart = input("Type next to allow the next student to clock in: ").lower()
    if restart == "next":
        main()
    else:
        exit()

main()

