'''used Python 3.8
developed and tested by
Aleksander Tkachenko
mivotanaj@gmail.com'''


print('Please, input your distance in km. For example 12 or 15.455')
s = float(input())
print('Please, input the number of your mode of transportation on foot - 1, bike - 2, car - 3, bus - 4')
figure = input()
if figure == '1':
    t = s / 5
    h = int((t*60) // 60)
    m = int((t*60) % 60)
    print(h, 'h', m, 'min')
elif figure == '2':
    t = s / 30
    h = int((t*60) // 60)
    m = int((t*60) % 60)
    print(h, 'h', m, 'min')
elif figure == '3':
    t = s / 50
    h = int((t * 60) // 60)
    m = int((t * 60) % 60)
    print(h, 'h', m, 'min')
elif figure == '4':
    t = s / 40
    h = int((t*60) // 60)
    m = int((t*60) % 60)
    print(h, 'h', m, 'min')
else:
    print("This date is wrong. Please, try it again!")