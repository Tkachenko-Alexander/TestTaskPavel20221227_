''' Teсhnical task: create the number
sequence from 1 to 100. Where the number divisible by 3 will display "Fizz".
The number divisible by 5 will display "Buzz".
 A number divisible by 3 and 5 will display "Fizz Buzz"   '''

a = 5
b = 6
c = 7


p = (a + b + c) / 2

s = (p * (p - a) * (p - b) * (p - c)) ** 0.5

print(f'Площадь треугольника со сторонами {a}, {b} и {c} равняется {round(s, 2)}')