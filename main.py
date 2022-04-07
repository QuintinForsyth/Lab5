import random
import replit

def get_int(message):
  x = int(input(message))
  return(x)
  
def play(play_again):
  if (play_again == "yes" or play_again == "Yes" or play_again == "Y" or play_again == "y"):
      print("Reseting random number")
      replit.clear()
      play_game()
    

def guess_number(random_number, top_range, minimum_range):
  guess = int(input("Guess a number between "+str(minimum_range)+" and "+str(top_range)))
  if (guess == random_number):
    play_again = input("Correct!\nwould you like to play again (Y or N)?")
    play(play_again)

  elif(guess != random_number):
    play_again = input("wrong!\nwould you like to play again (Y or N)?")
    play(play_again)


  

def play_game():
  minimum_range = get_int("Enter the minimum number")
  top_range = get_int("Enter the maximum number")
  random_number = random.randint(minimum_range, top_range)
  guess_number(random_number, top_range, minimum_range)

play_game()