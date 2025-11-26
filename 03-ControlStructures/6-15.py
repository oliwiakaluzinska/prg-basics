number = int(input("Enter EAN-13 article number: "))
if len(str(number)) == 13:
    print("Article number is correct")
    if str(number)[:3] == "590":
        print("Article manufactured in Poland")
    else:
        print("Article not manufactured in Poland")
else:
    print("Article number is not correct") 