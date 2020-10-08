students_list = ["ethan bishop", "india ward", "charles mardis", "joseph dandan", "lathe ward", "seth hogue", "jeremiah tatum", "travis alexander", "sean coh", "loveen kaur", "kenia sandoval", "lance easley", "gregory bowles",
 "dylan mccreary", "aj hardaway", "al dees", "asiah moton", "bryce taylor", "jeremiah bass", "evan sanders", "matthew wilson", "andy duarte"]
instructors_list = ["nate clark", "fernae ellard", "corey mize"]
def input_name():
    while True:
        name = input("Name (First Last): ").lower()
        if name in students_list:
            print("Successfully Logged In!")
            return name
        else: 
            print("Please Provide A Valid Name!")


def input_instructor_name():
    while True:
        instructor_name = input("Instructor Login (First Last): ").lower()
        if instructor_name in instructors_list:
            print("Login Successfull! Access Granted!")
            return instructor_name 
        else:
            print("Login Failed! Access Denied. Retry Login.")