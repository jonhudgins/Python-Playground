# by jon hudgins and jackie faselt 

import json

with open('superheroes.json', 'r') as f:
    superheroes = json.load(f)
    
# print(superheroes)


# creates an empty array called powers 
powers = []

# Loop through the members of the squad and 

# append the powers of each to the powers array 

members = superheroes['members']
for member in members:
	this_members_powers = member['powers']
	powers.append(this_members_powers)

# prints those powers to the terminal 
print(powers)