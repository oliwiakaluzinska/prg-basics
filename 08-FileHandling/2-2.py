seven_wonders = [
   "Great Wall of China",
   "Petra",
   "Christ the Redeemer",
   "Machu Picchu",
   "Chichen Itza",
   "Roman Colosseum",
   "Taj Mahal"
]

# Name of the file to write to
file_name = 'seven_wonders.txt'

# Sort data alphabetically
seven_wonders_sorted = sorted(seven_wonders)

# Write data to the file
with open(file_name, 'w') as file:
      for wonder in seven_wonders_sorted:
        file.write(wonder + '\n')
        
with open(file_name, 'r') as file:
    content = file.read()

print("Contents of the file:")
print(content)