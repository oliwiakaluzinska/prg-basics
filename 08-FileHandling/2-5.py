shopping_list = 'shopping_list.txt'

# adds product name at the end of a shopping list
def add_product(file_name, product_name):
   with open(shopping_list,'a') as file:
      ... .write(file)

# Takes next product name from the keyboard
product = ""
while product != "0":
   product = input('Enter product name (0 stops): ')
   if product == '0':
      ... # stops entering food names ('while' breaks)
   else:
      add_...