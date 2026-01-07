import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"              # brackets not correct

def brackets_ok(expression):
   brackets = queue.LifoQueue()
   pairs = {')':'(', '}':'{', ']':'['}
   for i in expression:
      if i in '[{(':
        brackets.put(i)
      elif i in ')]}':
         if brackets.empty():
           return False
         if brackets.get() != pairs[i]:  # sprawdzamy dopasowanie
                return False
      
   
   return brackets.empty()#True if brackets in expression are ok of False otherwise

if brackets_ok(expression1):
   print("Expression brackets are correct.")
else:
   print('"Expression brackets are not correct."')

if brackets_ok(expression2):
   print("Expression brackets are correct.")
else:
   print("Expression brackets are not correct.")

if brackets_ok(expression3):
   print("Expression brackets are correct.")
else:
   print("Expression brackets are not correct.")