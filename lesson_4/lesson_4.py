age = int(input('Сколько вам полных лет? '))
name = input('Как вас зовут? ')

if age <= 0:
    print(f'{name}, вы еще не родились.')
elif age <= 6:
    print(f'{name}, вы ребенок.')
elif age <= 18:
    print(f'{name}, вы подросток.')
elif age <= 60:
    print(f'{name}, вы взрослый.')
elif age <= 90:
    print(f'{name}, вы пожилой.')
else:
    print(f'{name}, вы долгожитель.')
