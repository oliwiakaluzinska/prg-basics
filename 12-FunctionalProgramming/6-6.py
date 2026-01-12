data = [("Smith","Lucy"),("Jones","Janet"),("Lee","Jerry"),
   ("Jackson","Peter"),("Johnson","Rick"),
   ("Lewis","Terry"),("Clarke","Robin")]

mean = list(map(lambda x:x[0].upper()+","+x[1], data))

print("\n".join(mean))