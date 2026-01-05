files_content = 'it_company.csv'

with open(files_content, 'r', encoding='utf-8') as file:
    names = file.read()

for i in names:

