print("Welcome to HORROR CITY!, PLEASE ANSWER THE FOLLOWING QUESTION OIN ORDER TO COME IN!!!")

fistName = input ("Please write your name : ")
lastName = input ("Please write your last name : ")
age = int (input ("Please write your age : "))
birthYear = int (input ("Please write your birth of year : "))

personInfo = [fistName, lastName, age, birthYear]

for i in personInfo:
    print(i)

if (personInfo[2] < 18):
    print("You can't go out because it's too dangerous!")
else:
    print("You can go out to street.")
