#програма для розрахунку типових математичних задач з процентами

print('Введіть умову задачі(цифру) наприклад: 1\n1. Знайти % від числа\n2. Знайти число а, коли відомо що % від нього = b\n3.Знайти % відносно числа')
umova = int(input())

if umova == 1:
	print('Знайти % від числа')
	a = int(input('Введіть число від якого потрібно знайти %:'))
	p = int(input('Введіть %:'))
	vidpov1 = a/100*p
	print(vidpov1)

if umova == 2:
	print('Знайти число а, коли відомо що % від нього = b')
	p = int(input('Введіть %:'))
	b = int(input('Введіть число b:'))
	vidpov2 = b/p*100
	print(vidpov2)

if umova == 3:
	print('Знайти % відносно числа:')
	a = int(input('Введіть число a:'))
	b = int(input('Введіть число b:'))
	vidpov3 = (a/b)*100
	print(vidpov3)