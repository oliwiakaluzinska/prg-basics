import csv

def print_graphic_designers(filename):
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        print("GRAPHIC DESIGNERS")
        print("=================")
        
        for row in reader:
            # Sprawdzamy, czy w kolumnie "Job Title" jest Graphic Designer
            if row["Job Title"] == "Graphic Designer":
                first_name = row["First Name"]
                last_name = row["Last Name"]
                email = row["Email"]
                print(f"{first_name} {last_name},{email}")

print_graphic_designers("it_company.csv")