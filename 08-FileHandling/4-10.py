import csv

def f(tekst):
    with open(tekst, mode ='r', encoding='utf-8') as file:
        product = list(csv.DictReader(file))
        print('Products which price is less then 60:')
        for i in product:
          if float(i['Price']) < 60:
            print(i['Product_Name'])
        
        print('Products which stock is less then 40:')
        for j in product:
           if int(j['Stock_Quantity']) < 40:
              print(j['Product_Name'])

f('clothing.csv')