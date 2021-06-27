import constants

teams = constants.TEAMS[::]
players = constants.players[::]
length_of_teams = len(teams)
num_of_player = len(players)
players_per_team = num_of_player_per_team = num_of_player / length_of_teams
# {'Gorillas": [{ }, { }, { }], 'Bats": [{ }, { }, { }], 'Monkeys": [{ }, { }, { }]}
teams_with_players = {}

for team in teams:
    teams_with_players[team] = []

print('BASKETBALL TEAM STATS TOOL')
print('\n')


while True:
    print('====MENU====')
    print('\n')
    print('Here are your choices:')
    print('1) Display Stats')
    print('2) Quit')
    print('\n')
    user_option_choice = input('Enter An Option --> ')
    try:
        if user_option_choice == 1:
            team_index = 0
            num = 0
            for player in players:
                print(player)
                if(len(teams_with_players[teams[team_index]]) !=6):
                    curr_team = teams_with_players[teams[team_index][' ']]
                    print(curr_team)
                    # curr_team[0][player['name']] = player
                    print(teams_with_players)
        elif user_option_choice == 2:
                print("Goodbye")
                break
    except ValueError:
        break

if __name__ == '__main__':
    print(players[0])

teams_with_players[teams[team_index]['name']]
