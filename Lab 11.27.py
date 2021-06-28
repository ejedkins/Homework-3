player_dict = {}
#Part 1 -
for i in range(1, 6):
       print("Enter player " + str(i) + "'s jersey number:")
       jersey_num = int(input())
       print("Enter player " + str(i) + "'s rating:")
       rating = int(input())

       if jersey_num < 0 and jersey_num > 99 and rating < 0 and rating > 9:
            print('invalid entry')
            break
       else:
            player_dict[jersey_num] = rating
#Part 2-
    print("MENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit")
    print()


option=''
while (option.upper()!='q'):
    print('\nMENU\na - Add player\nd - Remove player\nu - Update player rating\n'
          'r - Output players above a rating\no - Output roster\nq - Quit\n')

    option = input('Choose an option:\n')

    #if the input is a, a player is added to the list
    if (option == 'a'):
        jersey_num = int(input('Enter a new player\'s jersey number:\n' .format(i)))
        rating = int(input('Enter the players\'s rating:\n'.format(i)))
        player_dict[jersey_num] = rating

    #If the input is d, a player is deleted from the list
    elif (option == 'd'):
        jersey_num = int(input('Enter a jersey number:\n'))
        if jersey_num in player_dict.keys():
            del player_dict[jersey_num]

    #If the input is u, a player rating is updated
    elif (option == 'u'):
        jersey_num = int(input('Enter a jersey number:\n'))
        if jersey_num in player_dict.keys():
            rating = int(input('Enter a new rating for player:\n'))
            player_dict[jersey_num] = rating

    #If the input is r, the rating of player are given
    elif (option == 'r'):
        rating_input=int(input('Enter a rating:\n'))
        print('ABOVE {}'.format(rating_input))
        for jersey_num,rating in sorted(player_dict.items()):
            if rating > rating_input:
                print("Jersey number: %d, Rating: %d" % (jersey_num,rating))

    #If the input is o, the roster of the team should be printed
    elif (option == 'o'):
        print("ROSTER")
        for jersey_num,rating in sorted(player_dict.items()):
            print("Jersey number: %d, Rating: %d" % (jersey_num,rating))
