def play_game():
  player1_name = input("Enter player1 name:")
  player2_name = input("Enter player2 name:")
  print("1.Rock")
  print("2.Paper")
  print("3.Scissor")
  choice1=int (input("Enter player1 choice:"))
  choice2=int (input("Enter player2 choice:"))
  if(choice1==1 and choice2==2):print(f'{player2_name} won!')
  elif(choice1==1 and choice2==3):print(f'{player1_name} won!')
  elif(choice1==2 and choice2==1):print(f'{player1_name} won!')
  elif(choice1==2 and choice2==3):print(f'{player2_name} won!')
  elif(choice1==3 and choice2==1):print(f'{player2_name} won!')
  elif(choice1==3 and choice2==2):print(f'{player1_name} won!')
  elif(choice1==choice2):print("Tie!")
  else:print("Invalid input!")
play_game()

def play_again():
  while True:
    print("Do you want to play again?")
    Ans = input("Yes or no").lower()
    if(Ans=='yes'):
      play_game()
    else:print("Thank you for playing!")
    break
play_again()

