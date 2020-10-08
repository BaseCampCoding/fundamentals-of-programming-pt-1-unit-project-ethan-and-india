import ESSENTIAL_FUNCTIONS
print("Good Morning, This program will allow you the instructor\nto see when your students clocked in for the day.")
instructor_login = ESSENTIAL_FUNCTIONS.input_instructor_name()
while True:
    student_clock_in_time = input("Would you like to see the times your students clocked in? If so (Type Y or N): ").lower()
    if student_clock_in_time == "y":
        f = open("LOGINTIMES.txt", "r")
        print(f.read())
        break
    elif student_clock_in_time == "n":
        print("Come back When you are ready!")
        quit()
    else:
        print("Invalid Response Try Again.")
while True:
    clearing_txt_file = input("Would you like to clear the times to prepare for the next day?\nIf so just type clear or type quit to exit the program\n-without deleting the LOGINTIMES.txt.: ").lower()
    if clearing_txt_file == "clear":
        file = open("LOGINTIMES.txt","r+")
        file.truncate(0)
        file.close()
        print("File Successfully Cleared. Logging Out.")
        break
    elif clearing_txt_file == "quit":
        print("Quitting Program!")
        quit()
    else: 
        print("Please Type clear or quit")

