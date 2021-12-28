import sys
from helpers import (define_customizations, check_num_players,
get_character_bounds, get_vehicle_bounds, apply_bonuses, gen_combination)
from termcolor import colored

print("-------------------------------------------------------------------------------------------------")
print()
print(colored("\t\t\tWelcome to the Mario Kart Character/Vehicle Randomizer!",
              "cyan"))
print()
print("-------------------------------------------------------------------------------------------------")

args = []
#split arguments received from command line by space, ignore leading whitespace
if len(sys.argv) > 1:
    args = sys.argv[1].split(" ")[1:]
#if the user does not have any flags, let them know about the help message
if len(args) == 0:
    print("Type ./kart --help to explore randomizer customizations!")
    print()
arg_index_dict = {}
i = 0
#make a dictionary of flags and their indices
for arg in args:
    arg_index_dict[arg] = i
    i += 1
characters, vehicles, num_p, players = define_customizations(args,
                                                             arg_index_dict)
check_num_players(players, num_p)
lower_bound_c, upper_bound_c = get_character_bounds(characters)
lower_bound_v, upper_bound_v = get_vehicle_bounds(vehicles)
#store the bounds for our randomizer in a dictionary so we do not have to pass
#in four separate args
bounds = {
    "lc": lower_bound_c,
    "uc": upper_bound_c,
    "lv": lower_bound_v,
    "uv": upper_bound_v
}
summary = {}
#generate a random character/vehicle combo based on the flags the user provided
for player in players:
    character_text, vehicle_text = gen_combination(player, arg_index_dict,
                                                   bounds)
    summary[player] = player + ": " + character_text + " -> " + vehicle_text

if "-f" in arg_index_dict:
    print("FAST MODE")
for player_info in summary:
    print(summary[player_info])
