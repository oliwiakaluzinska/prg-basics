total_washing_time = 0
program = input('Select washing program: (j)acket, (u)nderwear, (s)hoes:')
extra_rinse = input('Extra rinse? (y/n)')
extra_spin = input('Extra spin? (y/n)')
if program == 's':
    print('Washing product: shoes')
    total_washing_time += 20
elif program == 'u':
    print('Washing product: underwear')
    total_washing_time += 70
elif program == 'j':
    print('Washing product: jacket')
    total_washing_time += 40

if extra_rinse == 'y':
    extra_rinse = True
    total_washing_time += 15
else: 
    extra_rinse = False
print(f'Extra rinse: {extra_rinse}')
if extra_spin == 'y':
    extra_spin = True
    total_washing_time += 9
else: 
    extra_spin = False
print(f'Extra spin: {extra_spin}')

print(f'Total washing time is {total_washing_time} min')