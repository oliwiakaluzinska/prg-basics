def f1(text):
    count = 0
    text = str(text)
    text = text.split()
    for i in text:
        count += 1
    return count

def f2(text):
    text = str(text)
    text = text.split()
    array = []

    while len(text) > 0:
      max = ""
      for i in text:
        if len(i) > len(max):
            max = i
      array.append(max)
      text.remove(max)
    return ",".join(array)

def f3(text):
   text = str(text)
   text = text.split()
   array = []
   for i in text:
      array.append(i)
   array = sorted(array)
   return ",".join(array)

if __name__ == "__main__":
    print(f1('An apple a day keeps the doctor away'))
    print(f2('An apple a day keeps the doctor away'))
    print(f3('An apple a day keeps the doctor away'))