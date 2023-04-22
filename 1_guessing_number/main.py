import random

random_number=random.randint(1, 100)
#print(random_number)

game_count=1
while True:
    try :
        my_number=int(input('enter a number'))
        if my_number > random_number:
            print('down')
        elif my_number < random_number:
            print('up')
        else:
            print(f'wow game_count : {game_count}')
            break

        game_count += 1
    except:
        print('please enter only number')