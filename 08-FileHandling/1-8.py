def read_from_file(name):
   with open(name) as file:
      content = file.read()
   return content

file_content = read_from_file('pets.txt')
print(file_content)

file_lines = file_content.splitlines()

total_words = 0

for line in file_lines:
   words_in_line = line.split()
   total_words += len(words_in_line)

print("\nTotal number of words:", total_words)
