# file names
employees_file = 'it_company.csv'
position_file = 'software_engineer2.txt'

# Position
job_title = 'Software Engineer'

# write selected employees to a file
with open(employees_file, 'r') as file:
   with open(position_file, 'w') as files:
      for line in file:
         if job_title in line:
            files.write(line)