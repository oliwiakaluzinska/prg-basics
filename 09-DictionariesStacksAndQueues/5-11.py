import json
file_name = 'votes.json'

try:
 with open(file_name, 'r') as file:
    votes = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
   votes = {}
   
person_name = input('Name of the person you are voting for:')
if person_name in votes:
    votes[person_name] += 1
else:
    votes[person_name] = 1

with open(file_name, 'w') as file:
   json.dump(votes, file)
