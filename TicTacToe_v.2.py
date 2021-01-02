import random

while True:
    def full_game():
        game_array = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        board_sample = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        filled_squares = []
        # i = 0  # turn counter

        def print_board_sample():
            print()
            print(board_sample[0], '|', board_sample[1], '|', board_sample[2])
            print('---------')
            print(board_sample[3], '|', board_sample[4], '|', board_sample[5])
            print('---------')
            print(board_sample[6], '|', board_sample[7], '|', board_sample[8])
            print()

        def game_board():
            print()
            print(game_array[0], '|', game_array[1], '|', game_array[2])
            print('---------')
            print(game_array[3], '|', game_array[4], '|', game_array[5])
            print('---------')
            print(game_array[6], '|', game_array[7], '|', game_array[8])
            print()

        print('\nWelcome to TicTacToe! Here are the instructions \n')
        print('The game board looks like this: \n')
        print_board_sample()
        print('\nEach square has a corresponding index. To play your marker, type the index number of the square.')
        print('\nWould you like to play against the computer or another person?')
        game_mode = input('Computer or Human?')

        print('\nLet\'s play!')

        def human_vs_human():

            turn = 'X'
            i = 0
            while i <= 9:

                player_input = input(
                    '\nPlayer %s, which square would you like?' % (turn))

                if player_input.isalpha() == True or int(player_input) not in list(range(1, 10)):
                    print(
                        '\nThat is not a valid input. Please try again. Remember, the squares are labeled from 1-9 based on this picture: \n')
                    print_board_sample()

                elif game_array[int(player_input) - 1] == 'X' or game_array[int(player_input) - 1] == 'O':
                    print('\n That square is filled already. Try another square!')

                else:
                    game_array[int(player_input) - 1] = turn
                    i += 1
                    game_board()

                    if turn == 'X':
                        turn = 'O'

                    elif turn == 'O':
                        turn = 'X'

                if game_array[0] == game_array[1] == game_array[2] != ' ':  # top row
                    print('\nGame over! Player %s wins!' % (game_array[0]))
                    break

                elif game_array[3] == game_array[4] == game_array[5] != ' ':  # middle row
                    print('\nGame over! Player %s wins!' % (game_array[3]))
                    break

                elif game_array[6] == game_array[7] == game_array[8] != ' ':  # bottom row
                    print('\nGame over! Player %s wins!' % (game_array[6]))
                    break

                elif game_array[0] == game_array[3] == game_array[6] != ' ':  # left column
                    print('\nGame over! Player %s wins!' % (game_array[0]))
                    break

                elif game_array[1] == game_array[4] == game_array[7] != ' ':  # middle column
                    print('\nGame over! Player %s wins!' % (game_array[1]))
                    break

                elif game_array[2] == game_array[5] == game_array[8] != ' ':  # right column
                    print('\nGame over! Player %s wins!' % (game_array[2]))
                    break

                elif game_array[0] == game_array[4] == game_array[8] != ' ':  # diagonal
                    print('\nGame over! Player %s wins!' % (game_array[0]))
                    break

                elif game_array[2] == game_array[4] == game_array[6] != ' ':  # diagonal
                    print('\nGame over! Player %s wins!' % (game_array[2]))
                    break

                elif i == 9:
                    print('Tie Game!')
                    break

        def human_vs_computer():

            player = input('What is your name?')

            computer = 'O'
            i = 0
            while i <= 9:

                player_input = input(
                    '\n%s, your turn! Which square would you like?' % (player))

                if player_input.isalpha() == True or int(player_input) not in list(range(1, 10)):
                    print(
                        '\nThat is not a valid input. Please try again. Remember, the squares are labeled from 1-9 based on this picture: \n')
                    print_board_sample()

                elif game_array[int(player_input) - 1] == 'X' or game_array[int(player_input) - 1] == 'O':
                    print('\n That square is filled already. Try another square!')

                else:
                    game_array[int(player_input) - 1] = 'X'
                    i += 1

                    while i < 9:
                        computer_turn = random.randint(1, 9)
                        if game_array[computer_turn - 1] == ' ':
                            game_array[computer_turn - 1] = 'O'
                            print('\nComputer plays square %i.' %
                                  (computer_turn))
                            game_board()
                            i += 1
                            break
                        else:
                            continue

                if game_array[0] == game_array[1] == game_array[2] != ' ':  # top row
                    print('\nGame over! Player %s wins!' % (game_array[0]))
                    game_board()
                    break

                elif game_array[3] == game_array[4] == game_array[5] != ' ':  # middle row
                    print('\nGame over! Player %s wins!' % (game_array[3]))
                    game_board()
                    break

                elif game_array[6] == game_array[7] == game_array[8] != ' ':  # bottom row
                    print('\nGame over! Player %s wins!' % (game_array[6]))
                    game_board()
                    break

                elif game_array[0] == game_array[3] == game_array[6] != ' ':  # left column
                    print('\nGame over! Player %s wins!' % (game_array[0]))
                    game_board()
                    break

                elif game_array[1] == game_array[4] == game_array[7] != ' ':  # middle column
                    print('\nGame over! Player %s wins!' % (game_array[1]))
                    game_board()
                    break

                elif game_array[2] == game_array[5] == game_array[8] != ' ':  # right column
                    print('\nGame over! Player %s wins!' % (game_array[2]))
                    game_board()
                    break

                elif game_array[0] == game_array[4] == game_array[8] != ' ':  # diagonal
                    print('\nGame over! Player %s wins!' % (game_array[0]))
                    game_board()
                    break

                elif game_array[2] == game_array[4] == game_array[6] != ' ':  # diagonal
                    print('\nGame over! Player %s wins!' % (game_array[2]))
                    game_board()
                    break

                elif i == 9:
                    print('\nTie Game!')
                    game_board()
                    break

        if game_mode.lower() == 'human':
            human_vs_human()

        elif game_mode.lower() == 'computer':
            human_vs_computer()

    full_game()

    play_again = input('Do you want to play again? [y/n]')

    if play_again.lower() == 'y':
        continue

    else:
        print('Thanks for playing, Good-Bye!')
        break
