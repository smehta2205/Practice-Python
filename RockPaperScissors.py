counter = 0
global player1
global player2
global p1
global p2
p1 = 0
p2 = 0

def rules():
	print('Rock smashes Scissor, Scissor cuts Paper, Paper covers Rock \n')

def takeInputp1():
	global player1
	player1 = int(input('Player1 enter your choice: Rock[1], Paper[2], Scissor[3] \n'))
	print('')

	if(player1>3 or player1<1):
		print('Enter a number between 1 and 3\n')
		takeInputp1()

def takeInputp2():
	global player2
	player2 = int(input('Player2 enter your choice: Rock[1], Paper[2], Scissor[3]\n'))
	if(player2>3 or player2<1):
		print('Enter a number between 1 and 3\n')
		takeInputp2()

def compare():
	global p1
	global p2
	global player2
	global player1
	if(player1==1):
		if(player2==2):
			print('Player2 wins')
			p2+=1
		if(player2==3):
			print('Player1 wins')
			p1+=1
		if(player2==1):
			print("It's a draw!!!")

	if(player1==2):
		if(player2==3):
			print('Player2 wins')
			p2+=1
		if(player2==1):
			print('Player1 wins')
			p1+=1
		if(player2==2):
			print("It's a draw!!!")

	if(player1==3):
		if(player2==1):
			print('Player2 wins')
			p2+=1
		if(player2==2):
			print('Player1 wins')
			p1+=1
		if(player2==3):
			print("It's a draw!!!")

def displayScore():
	global p1
	global p2
	print("Player1 score: {}, Player2 score: {} \n".format(p1, p2))

def playAgain():
	play = input('Do you want to play again, Yes[y] or No[n]\n')
	if play in ['y', 'Yes','yes']:
		mainfunc()
	elif play in ['n','No','no']:
		final()
		quit()
	else:
		print('Please enter a valid input')
		playAgain()

def final():
	global p1
	global p2
	if(p1>p2):
		print('Player1 is the overall winner')
		displayScore()
	elif(p2>p1):
		print('Player2 is the overall winner')
		displayScore()
	else:
		print("It's a draw")
		displayScore()



def mainfunc():
	global counter
	if(counter==0):
		rule = input('Would you like to know the rules, Yes[y] or N[n]\n')
		if rule in ['y', 'Yes','yes']:
			rules()
		elif rule in ['n','No','no']:
			pass
		else:
			print('Please enter a valid input')
			main()

	takeInputp1()
	takeInputp2()

	compare()

	displayScore()

	counter+=1

	playAgain()

mainfunc()