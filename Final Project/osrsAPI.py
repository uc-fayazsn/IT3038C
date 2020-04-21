from OSRS_Hiscores import Hiscores
import pandas as pd 

# User to lookup
input = input("Enter username of the account you're looking for : ")
username = input


# Initialize user object, if no account type is specified, we assume 'N'

user = Hiscores(username, 'IM')



# Get the entire stat dictionary

user.stats


# # Get total Levels

# user.skill('total')



# # Get a specific skill's ranking, level, and experience

# user.stats['runecrafting']



# # Get skill's level, ranking, and experience separately

# user.stats['runecrafting']['level']

# user.stats['runecrafting']['rank']

# user.stats['runecrafting']['experience']




# # A simpler way to just get a skill's attributes

# print("Stats gathered are for the account" + " " + username) 


# print("Current Attack Level level:", user.skill('attack', 'level'))

# print("Current rank:", user.skill('attack', 'rank'))

# print("Current exp:", user.skill('attack', 'experience'))

# print("Exp remaining:", user.skill('attack','exp_to_next_level'))


df = pd.DataFrame()

#df['Stats'] = user

overall = user.skill('total')
df['Overall'] = overall

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


df.to_csv('C:\IT3038C\FinalProject\APItestpull.csv')
