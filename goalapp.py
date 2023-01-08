name = input('Enter your name: ')
y_old = int(input('What year are we in? '))
if y_old > 2022:
    print(f'Happy New year {name}. It is {y_old}')
else:
    print(f'New year is coming soon {name}.')
goals = input("'List down one big new year  resolutions:")
alam = input(f'Should we remind you of {goals}? ')
if alam == 'yes':
    print('Awesome! You will make it this year.')
else:
    print('Cheers! Happy New Year. Remember to create a new you!')
