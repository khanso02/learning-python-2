#not yet finished, but rock paper scissors


try:
	From random import *
	player_move= raw_input("Rock paper scissors?")
	computer_move = 0
	outcome= None
computer_move = randint(1,3)
	if computer_move == 1:
	computer_move= 'rock'
	if computer_move == 2:
	computer_move = 'scissors'
	if computer_move == 3:
	computer_move = 'paper'
if player_move = rock and computer_move = rock:
	outcome = 'Tie'
if player_move = 'rock' and computer_move = 'paper':
	outcome = 'Loss'
if player_move = 'rock' and computer_move = 'scissors':
	outcome = 'Win'
if player_move = 'paper' and computer_move = 'rock':
	outcome = 'Win'
if player_move = 'paper' and computer_move = 'paper':
	outcome = 'Tie'
if player_move = 'paper' and computer_move = 'scissors':
	outcome = 'Loss'
if player_move = 'scissors' and computer_move = 'scissors':
	outcome = 'Tie'
if player_move = 'scissors' and computer_move = 'paper':
	outcome = 'Win'
if player_move = 'scissors' and computer_move = 'rock':
	outcome = 'Loss'

except:
	print "error"
print outcome

closeInput = raw_input("Press ENTER to exit")
print "Closing..."
