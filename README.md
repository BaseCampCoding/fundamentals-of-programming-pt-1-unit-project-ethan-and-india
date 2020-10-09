# README

# Student Clock-In Program, With Admin Access to Clock-in Times. Created in Python.

## Core Concept:

The main Idea of this entire program was to create a more seamless clocking in process for students or even employees. With this program A student/employee with enter their name (First the n Last) if a name is incorrect it will prompt the user to try again. If a student clocks in late it will notify them that are late past any specific deadline that they have to be at school. However this is just a very base program that lots of features and different preferences could be added. This also includes a secondary program that will allow an admin to login and check all of the students and the times that they have clocked in. The admin program will also allow an instructor clear that file to prepare for the next day.

## Technical Breakdown & Example Code:

### Example:
#### Student.py
Good Morning, Welcome to Class! Please Sign in!

Name (First Last): rtadn bishop

Please Provide A Valid Name!

Name (First Last): Ethan Bishop

Successfully Logged In!

Are you ready to clock in. If so type (clock-in): clock-in

You have clocked in   : 09-Oct-2020 (09:03:26.445138)

It's past 8:15 A.M YOU ARE LATE!

Type next to allow the next student to clock in: next

Good Morning, Welcome to Class! Please Sign in!

#### admin.py
Good Morning, This program will allow you the instructor

to see when your students clocked in for the day.    

Instructor Login (First Last): nte clark

Login Failed! Access Denied. Retry Login.

Instructor Login (First Last): Nate Clark

Login Successfull! Access Granted!

Would you like to see the times your students clocked in? If so (Type Y or N): Y

ethan bishop

 Clocked In at 09-Oct-2020 (09:03:26.445138)

seth hogue

 Clocked In at 09-Oct-2020 (09:04:17.894095)

matthew wilson

 Clocked In at 09-Oct-2020 (09:05:26.130915)

Would you like to clear the times to prepare for the next day?

If so just type clear or type quit to exit the program

-without deleting the LOGINTIMES.txt.: clear

File Successfully Cleared. Logging Out.

#### Technical Explanation:
The main branch of this program is on a page titled [students.py](http://students.py). This contains the main loop within our program that allows the students to clock-in if they are registered on the list. This list and a couple of our main functions were imported from a separate file titles ESSENTIAL_FUNCTIONS.py which includes a couple validation loops and both the lists of instructors and students. These lists can be modified to fit any applicable needs. The last two files that are included within this program are the [admin.py](http://admin.py) and LOGINTIME.txt. [Admin.py](http://admin.py) is the admin program which could be moved into a function and imported into one main page but for this we separated them for ease of access. The logintimes file is simply just a txt file that the student clock-in times are printed to and then accessed by admin.py and can also be cleared by typing a simple clear command.

## Overall Summary:

With this program we had hoped to achieved just creating something that made clocking in and viewing clock in times for instructors easier. There is a lot more that could be added to this program depending on specific needs/wants. If more time was allowed a lot more could've have been accomplished. Using certain modules that we didn't understand was quite the speedbump but eventually got figured out in the end. Hopefully anyone who cares to develop this program more adds some interesting features that will allow for more flexibility.
