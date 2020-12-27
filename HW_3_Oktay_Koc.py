import random
number = random.randint(0,100)
# print(number)
print("Welcome to the your game of life !!!)")
nameInfo = input ("Please write your full name : ")
print("Welcome " + str(nameInfo) + "\n You suppose to guess a number that is from 0 to 100")
i=1
while i !=1000:
	yourGuess = int(input ("What is the NUMBER in my MIND? :"))
	if number == yourGuess:
		print ("BINGO! YOU ARE RIGHT!, BYE BYE !!! ")
		i = 1000
		break
	else:
		print ("Nice try! But not enough! Keep guessing!\n")