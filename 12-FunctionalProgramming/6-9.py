temperatures = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}

result = list(filter(lambda x:temperatures[x]>0, temperatures))

print(result)