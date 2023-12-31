def part_one(input_game): 
    
    allowed = {'red': 12, 'green': 13, 'blue': 14}

    valid_games = []

    for line in input_game:
        game_id = line[5]
        result = True
        for game in line[8:].split('; '):
            print(game_id)
            colours = [(col.split(' ')) for col in game.split(', ')]
            for colour in colours:
                check = {colour[1] : colour[0]}
                print(check, int(colour[0]) <= allowed[colour[1]])
                if int(colour[0]) > allowed[colour[1]]:
                    result = False 
                    print('move on to next game')
            # break 
            print('')
        print('')

        # for game in line: #input_game[8:].split('; '):
        #     for s in game.split(', '):
        #         check = s.split(' ')
        #         if allowed[check[1]] >= int(check[0]):
        #             valid_games.append(input_game[5])
        #             print(check)

        #draws.append(draw)
        # print(game)
    
    return valid_games



def main(): 
    
    # input_file = '..//inputs//two.txt'

    # with open(input_file, 'r') as f:
    #     lines = [] 
    #     for line in f: 
    #         lines.append(line.rstrip('\n')) 
    
    # print(lines[:2])

    sample = ['Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green','Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue','Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red', 'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red', 'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green']

    print(part_one(sample))

if __name__ == "__main__": 
    main()