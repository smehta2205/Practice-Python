# Michael Nyamande 2016
import getpass  #library to hide the user's input
moves = {"rock":1 ,"paper":2,"scissors":3}
def play(player):
    move = getpass.getpass("{}'s move:    ".format(player))
    if move in moves:
        return moves[move] #return numeric value of move
    print("Invalid Move")
    play(player) #Recursion

def compare(player1 ,player2):
    diff = player1 - player2
    if((diff%2==0 and diff<0) or (diff%2==1 and diff>0)):
        return True # Player 1 won
    else:
        return False # Player 2 won

while input("Wanna Play ?   ").lower() in ["y","yes"]:
    player1 = play("player1")
    player2 = play("player2")
    if (player1==player2):
        print("\nDraw \n")
    else:
        winner = "Player 1" if (compare(player1 ,player2)) else "Player 2"
        print(" \n{} won the game \n".format(winner))
print("Thank you for playing")