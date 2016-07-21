number = 58
guess = input("Guess my lucky number!")
while number != int(guess):
	if number < int(guess):
		print("Your guess was too high!")
		guess = input("Try again:")
	else number > int(guess):
		print("Your guess was too low!")
		guess = input("Try again:")
if number == int(guess):
	print("You got it right!")
	print("Game Over")
	