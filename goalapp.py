name = input('Enter your name: ')
y_old = int(input('What year are we in? '))
if y_old > 2022:
    print(f'Happy New year {name}. Congratulations, you made it to {y_old}')
else:
    print(f'New year is coming soon {name}. Sit tight.')
goals = input("'List down one big goal for the year 2023: ")
alam = input(f'Should we remind you of {goals}? ')
if alam == 'yes':
    print('Awesome! You will make it this year.')
else:
    print('Cheers! Happy New Year. Remember to create a new you!')
