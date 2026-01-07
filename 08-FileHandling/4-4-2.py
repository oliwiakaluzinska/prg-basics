def f(files_name, size=5):
    with open(files_name,) as file:
        lines = file.readlines()

    for i in range(0, len(lines), size):
        for line in lines[i:i + size]:
            print(line.rstrip())

        
        if i + size < len(lines):
            input("Press Enter key...")

f("it_company.csv")
