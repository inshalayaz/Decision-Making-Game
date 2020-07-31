print('Welcome to the decision making game')
name = input('What is your Name?: ')
age = input('What is Your Age?: ')


if int(age) > 13 :
    print(f'Hello {name} welcome to The Game you are eligibal to play')
    want_to_play = input('Do you want to play? ')
    if (want_to_play).lower() == 'yes' :
        print("Let's play!")
        
        left_or_right= input('Make your first choice in the world of Zombies... Left or Right (Left/Right)').lower()
        
        if left_or_right == 'left':
            ans = input('You found two weapons but you can only carry one. Which one would you like to pick. (Sword/Shotgun)').lower()
            
            if ans == 'sword':
                print('You saw a zombie coming towards you but as you have a sword you killed it quietly and survived \n Congrats You Survived and were rescued')
            elif ans == 'shotgun':
                print('You saw a zombie coming towards you but as you have a shotgun you killed it making a lot of noise and now a whole hord is coming after you.')
                direction = input('You have to run choose where to go. (Ally/House)').lower()
                if direction == 'ally':
                    print('You saw a car coming your way you called for help and it stopped to help you. \n You Survived and were rescued')
                else:
                    print('On your run towards the house you fell and were bit by the zombie. You turned into a walker. \n You were not able to survive')
            else:
                  print('You were to slow and were killed bt the zombies')
            
        elif left_or_right == 'right' :
            ans = input('You found a car to travel safely and you escaped the quarantine zone. \n Congrats You Survived').lower()
        else:
            print('You were to slow and were killed bt the zombies')
        
            
    else:
        print('Come again Soon')
    
else:
    print('Leave Noob Suckerrrr!!')
    