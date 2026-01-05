# file names
original_file = 'healthy_lifestyle.txt'
target_file = 'copy_healthy_lifestyle2.txt'

# read the content of the original file
with open(original_file, 'r') as file:
   content = file.read()

# write the content to the target file (copy)
with open(target_file, 'w') as file:
   file.write(content)