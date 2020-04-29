from OSRS_Hiscores import Hiscores

import pandas as pd 



# User to lookup

input = input("Enter username of the account you're looking for : ")

username = input



# Initialize user object, if no account type is specified, we assume 'N' for default, options are N, IM, HC, UM

user = Hiscores(username, 'IM')



# Get the entire stat dictionary

user.stats



# Initialize dataframe to export pulled data

df = pd.DataFrame()



# Baseline for user skill stats defined in the dataframe

df['Stats'] = user.stats



# Accounts total level defined in the dataframe

overall = user.skill('total')

df['Overall'] = overall







# From here on it is individually pulling each skill from the OSRS API, which can be found here: https://runescape.wiki/w/Application_programming_interface#Old_School_Hiscores


attack = user.stats['attack']['level']

df['attack'] = attack



defense = user.stats['defense']['level']

df['defense'] = defense



strength = user.stats['strength']['level']

df['strength'] = strength



hitpoints = user.stats['hitpoints']['level']

df['hitpoints'] = hitpoints



ranged = user.stats['ranged']['level']

df['ranged'] = ranged



prayer = user.stats['prayer']['level']

df['prayer'] = prayer



magic = user.stats['magic']['level']

df['magic'] = magic



cooking = user.stats['cooking']['level']

df['cooking'] = cooking



woodcutting = user.stats['woodcutting']['level']

df['woodcutting'] = woodcutting



fletching = user.stats['fletching']['level']

df['fletching'] = fletching


fishing = user.stats['fishing']['level']

df['fishing'] = fishing



firemaking = user.stats['firemaking']['level']

df['firemaking'] = firemaking


crafting = user.stats['crafting']['level']

df['crafting'] = crafting



smithing = user.stats['smithing']['level']

df['smithing'] = smithing


mining = user.stats['mining']['level']

df['mining'] = mining


strength = user.stats['strength']['level']

df['strength'] = strength



herblore = user.stats['herblore']['level']

df['Herblore'] = herblore




agility = user.stats['agility']['level']

df['agility'] = agility




thieving = user.stats['thieving']['level']

df['thieving'] = thieving




slayer = user.stats['slayer']['level']

df['slayer'] = slayer





farming = user.stats['farming']['level']

df['farming'] = farming





runecrafting = user.stats['runecrafting']['level']

df['runecrafting'] = runecrafting


hunter = user.stats['hunter']['level']

df['hunter'] = hunter



construction = user.stats['construction']['level']

df['construction'] = construction




#attempting to make it bring only 1 row, unsuccessful

pd.set_option('display.max_rows', 1)



# exporting the data from the dataframe into a CSV.

df.to_csv('C:\IT3038C\osrsAPI\TESTINGFinalProject\input.csv')