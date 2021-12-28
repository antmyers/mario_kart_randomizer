import random
import time
import sys
from data import characters, light_v, middle_v, heavy_v
from termcolor import colored, cprint

'''
    This function returns the bounds our randomizer will use for
    character selection. If the user did not specify the -c flag,
    we will choose from all available characters (1-26).
'''
def get_character_bounds(available_characters):
    lower_bound_c = 1
    upper_bound_c = 26
    if available_characters == "light":
        upper_bound_c = 8
    elif available_characters == "middle":
        lower_bound_c = 9
        upper_bound_c = 16
    elif available_characters == "heavy":
        lower_bound_c = 17
    return lower_bound_c, upper_bound_c

'''
    This function returns the bounds our randomizer will use for
    vehicle selection. If the user did not specify the -v flag,
    we will choose from all available vehicles (1-12).
'''
def get_vehicle_bounds(available_vehicles):
    lower_bound_v = 1
    upper_bound_v = 12

    if available_vehicles == "karts":
        upper_bound_v = 6
    elif available_vehicles == "bikes":
        lower_bound_v = 7
    return lower_bound_v, upper_bound_v

'''
    This function makes sure that the desired number of players matches the
    number of player names given.
'''
def check_num_players(players, num_players):
    if len(players) != int(num_players):
        print("ERROR: MISMATCHED NUMBER OF PLAYERS AND NAMES GIVEN")
        sys.exit(1)

'''
    This function applies stat bonuses to a player depending on which character
    they received. It will also take into account the starting vehicle stats
    when applying the bonuses. The return value for this function is a
    dictionary that contains the text output for each stat.
    For instance, if a stat is unchanged, it goes into the dictionary as such.
    If a stat is affected by a bonus, it goes in the dictionary as:
    STAT (+bonus) and the text will be green.
'''
def apply_bonuses(stats, bonuses):
    stat_texts = {}
    for stat in stats:
        stat_texts[stat] = stats[stat]
        if stat in bonuses:
            stat_texts[stat] += bonuses[stat]
            text_string = str(stat_texts[stat]) + "(+" + str(bonuses[stat]) + ")"
            stat_texts[stat] = colored(text_string, 'green')
        else:
            stat_texts[stat] = str(stat_texts[stat])
    return stat_texts

'''
    This function returns the customizations our randomizer will use based on
    the flags given to the bash script. We return the available characters,
    available vehicles, number of players, and an array with the player names.
'''
def define_customizations(args, arg_index_dict):
    available_characters = "all"
    if "-c" in arg_index_dict:
        available_characters = args[arg_index_dict["-c"] + 1]
    available_vehicles = "all"
    if "-v" in arg_index_dict:
        available_vehicles = args[arg_index_dict["-v"] + 1]
    num_players = 1
    if "-n" in arg_index_dict:
        num_players = args[arg_index_dict["-n"] + 1]
    players = ["Doug Dimmaclone 1"]
    if "-p" in arg_index_dict:
        players = []
        j = arg_index_dict["-p"] + 1
        while j < len(args) and len(players) < int(num_players):
            players.append(args[j])
            j += 1
    else:
        i = 2
        while len(players) < int(num_players):
            players.append("Doug Dimmaclone " + str(i))
            i += 1
    return available_characters, available_vehicles, num_players, players

'''
    This function does the heavy lifting for our program. A character/vehicle
    combination is chosen based on our input bounds. The character and vehicle
    dictionaries are imported from data.py
    We change the color of the output text based on the type of character
    chosen by the randomizer. If the user specifies the -f flag, we omit most
    of the output and instead only print the summary.
'''
def gen_combination(player, arg_index_dict, bounds):
    seed = random.seed(None)
    rand_character = random.randint(bounds["lc"], bounds["uc"])
    rand_vehicle = random.randint(bounds["lv"], bounds["uv"])

    character = characters[rand_character - 1]
    character_text = colored(character["name"], 'green')
    weight_color = ""
    if character["Weight"] == "light":
        weight_color = "cyan"
    elif character["Weight"] == "middle":
        weight_color = "yellow"
    else:
        weight_color = "red"
    weight_text = colored(character["Weight"], weight_color)
    if "-f" not in arg_index_dict:
        time.sleep(1)
        print(player + " is " + character_text + "!")
        print(character["name"] + " is a " + weight_text + " weight.")
        print()
    # if len(character["bonuses"]) > 0:
    #     print("Your bonuses are:")
    # for bonus in character["bonuses"]:
    #     print("\t" + bonus + ": " + str(character["bonuses"][bonus]))

    vehicle = {}
    if rand_character < 9:
        vehicle = light_v[rand_vehicle - 1]
    elif rand_character < 17:
        vehicle = middle_v[rand_vehicle - 1]
    else:
        vehicle = heavy_v[rand_vehicle - 1]
    vehicle_text = colored(vehicle["name"], "magenta")
    if "-f" not in arg_index_dict:
        time.sleep(2)
        print(player + " is driving the " + vehicle_text + "!")
        if vehicle["inside_drift"]:
            celebration = colored("inside", "green")
            print("It's " + celebration + " drifting let's goooooo")
        else:
            desolation = colored("outside", "red")
            print("Unfortunately it's " + desolation + " drifting... F")
        time.sleep(2)
        print()
        print("Here are your stats after applying character bonuses:")
        time.sleep(1)
        stats = apply_bonuses(vehicle["stats"], character["bonuses"])
        print('Speed\tWeight\tAcceleration\tHandling\tDrift\tOffroad\tMini-Turbo')
        print(stats['Speed'] + '\t' + stats['Weight'] + '\t'
              + stats['Acceleration'] + '\t\t' + stats['Handling']
              + '\t\t' + stats['Drift'] + '\t' + stats['Offroad'] + '\t'
              + stats['Mini-Turbo'])
        print()
        print("-------------------------------------------------------------------------------------------------")
        time.sleep(2)
    return character_text, vehicle_text
