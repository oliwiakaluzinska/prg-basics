cinema_seats = [
   ['A', 'A', 'B', 'A', 'A'],
   ['A', 'B', 'B', 'A', 'A'],
   ['A', 'A', 'A', 'A', 'B'],
   ['B', 'A', 'A', 'A', 'A'],
   ['A', 'B', 'A', 'A', 'A']
]

def seats_total(seats):
   total = 0
   for i in seats:
      for j in i:
         total += 1
   return total

def seats_available(seats):
   av = 0
   for i in seats:
      for j in i:
         if j == 'A':
            av += 1
   return av

def seats_booked(seats):
   bo = 0
   for i in seats:
      for j in i:
         if j == 'B':
            bo += 1
   return bo

def seat_status(seats, row, place):
   for i in seats:
      if i == seats[row-1]:
         for j in i:
            if j == i[place-1]:
               return j

print('CINEMA INFORMATION TABLE')
print('Total seats:',seats_total(cinema_seats))
print('Seats available:',seats_available(cinema_seats))
print('Seats booked:', seats_booked(cinema_seats))
print('Seat in row 1, place 1:', seat_status(cinema_seats,1,1))
print('Seat in row 5, place 5:', seat_status(cinema_seats,5,5))
print('Seat in row 3, place 5:', seat_status(cinema_seats,3,5))