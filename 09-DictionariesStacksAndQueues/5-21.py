movie = {
    'name':'Die hard',
    'year':2006,
    'nationality':'British',
    'type':'comedy',
    'popular':True
}

file_name = 'favourite.json'
import json
with open(file_name, 'w', encoding='utf-8') as file:
    json.dump(movie, file, indent=4)