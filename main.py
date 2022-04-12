import random


def get_int(message):
  x = int(input(message))
  return(x)
  """
  gets integer from user
  """
  
def play():
  again = input("Correct!\nwould you like to play again (Y or N)?")
  if (again == "yes" or again == "Yes" or again == "Y" or again == "y"):
      print("\n"*150)
      print("Reseting random number")
      play_game()
  else:
    print("bye );")

def guess_number(random_number, top_range, minimum_range):
  guess = int(input("Guess a number between "+str(minimum_range)+" and "+str(top_range)))
  
  if (guess == random_number):
     return 

  print("Try again")
  guess_number(random_number, top_range, minimum_range)


  

def play_game():
  minimum_range = get_int("Enter the minimum number")
  top_range = get_int("Enter the maximum number")
  random_number = random.randint(minimum_range, top_range)
  guess_number(random_number, top_range, minimum_range) 
  play()
  

play_game()