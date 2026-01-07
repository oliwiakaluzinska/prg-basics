def display_file_in_chunks(filename, chunk_size=5):
    with open(filename,) as file:
        lines = file.readlines()

    for i in range(0, len(lines), chunk_size):
        for line in lines[i:i + chunk_size]:
            print(line.rstrip())

        if i + chunk_size < len(lines):
            input("Press Enter key...")

display_file_in_chunks("it_company.csv")


