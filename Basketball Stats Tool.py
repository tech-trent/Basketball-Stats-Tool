"""
Treehouse Python Techdegree
Project 2 - Basketball Stats Tool

"""

from constants import *
#Random module is only used for choosing players to sort into teams.
from random import choice 
#Math module is only used to tidy up the average height readout.                                   
from math import ceil                                               
cleaned_data = []

sorted_teams = {
    "Panthers": [],
    "Bandits": [],
    "Warriors": []
}

def clean_data():
    for player in PLAYERS:
        # New dictionary where clean data will be stored.
        new_dict = {}                                               
        for item in player:
            # Add name to the dictionary as-is.
            if item == "name":                                      
                new_dict.update(name = player[item])
            elif item == "guardians": 
                # Convert guardians string into list of 1 or 2 strings, then add it to the dictionary.
                guardians_list = player[item].split(" and ")       
                new_dict.update(guardians = guardians_list)
            elif item == "experience": 
                # Convert "YES"/"NO" into boolean and add it to the dictionary.
                if player[item] == "NO":                           
                    new_dict.update(experience = False)
                else:
                    new_dict.update(experience = True)
            # Convert first two characters of height string to a 2-digit integer and add it to the dictionary.
            else:                                                   
                new_dict.update(height = int(player[item][:2]))
        # Add the player's dictionary to the list of cleaned data.
        cleaned_data.append(new_dict)                               
def sort_teams():
    # Lists used to seperate players based on experience.
    experienced = []                                                
    inexperienced = [] 
    # Loop to seperate players based on experience using aforementioned lists.
    for player in cleaned_data:                                    
        if player["experience"]:
            experienced.append(player)
        else:
            inexperienced.append(player)
    # Loop indicating for each team it adds 3 experienced and 3 inexperienced players. Each name is removed from the list when added to a team to avoid "cloning".
    for team in sorted_teams:                                       
        selected_team = sorted_teams[team]
        for x in range(3):
            experienced_player = choice(experienced)
            inexperienced_player = choice(inexperienced)
            selected_team.append(experienced_player)
            selected_team.append(inexperienced_player)
            experienced.remove(experienced_player)
            inexperienced.remove(inexperienced_player)

# Simple function for filtering user input, pretty self-explanatory.
def handled_input(upper_bound : int):                               
    while True:
        try:
            response = int(input("\nEnter an option > "))
            if response < 1 or response > upper_bound:
                raise ValueError
            else:
                return response
        except:
            print(f"\nPlease type a whole number between 1 and {upper_bound}.")
        
# Dunder main block containing actual app behavior. `clean_data` and `sort_teams` are outside the loop to prevent the data from changing should the user decide to restart the program.
if __name__ == "__main__":                                                                                                  
    clean_data()
    sort_teams()

    while True:
        print(f"BASKETBALL TEAM STATS TOOL\n\n{'-' * 10} MENU {'-' * 10}\n\nOptions:\n\n 1. Display Team Stats\n 2. Quit")

        #  Teams are not re-sorted after reusing the program if user decides to quit or use/reuse the tool, and cleaned_data is not altered.      
        if handled_input(2) == 1:                                                                                           
            pass
        else:
            quit()

        # User selects team whose stats they want to view.
        print("\nWhich team? Options:\n\n 1. Panthers\n 2. Bandits \n 3. Warriors")                                         

        selected_team = handled_input(3)

        if selected_team == 1:
            selected_team = "Panthers"
        elif selected_team == 2:
            selected_team = "Bandits"
        else:
            selected_team = "Warriors"

        # Empty values indiciating each of which that must be filled to give a full statistical readout of the team.
        team_player_names = []                                                                                              

        experienced_count = 0

        inexperienced_count = 0

        cumulative_height = 0

        avg_height = 0

        team_guardians = []

        # Loop that sorts all needed data into the empty values and prepares them for printing.
        for player in sorted_teams[selected_team]:                                                                          
            for item in player:
                if item == "name":
                    team_player_names.append(player[item])
                elif item == "experience":
                    if player[item]:
                        experienced_count += 1
                    else:
                        inexperienced_count += 1
                elif item == "height":
                    cumulative_height += player[item]
                else:
                    for guardian in player[item]:
                        team_guardians.append(guardian)

        avg_height = ceil(cumulative_height / len(team_player_names))


        print(f"\nTeam: {selected_team} stats\n--------------------\n")
        print(f"Players on team: {len(team_player_names)}\n")
        print(f"Players:\n\n\t{', '.join(team_player_names)}\n")
        print(f"Experienced Players: {experienced_count}\n")
        print(f"Inexperienced Players: {inexperienced_count}\n")
        print(f"Average Height: {avg_height} inches\n")
        print(f"Guardians of Players:\n\n\t{', '.join(team_guardians)}\n")
        print("-" * 26 + "\n")
