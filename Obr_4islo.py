#Вывести число обратное по порядку введенному
n1 = int(input("Введите целое число: "))
n2 = 0

while n1 > 0:
    digit = n1 % 10 #находим остаток - последнюю цифру числа
    n1 = n1 // 10 #делим нацело - убираем последнюю цифру
    n2 = n2 * 10 #увеличиваем разрядность числа
    n2 = n2 + digit #добавляем очередную цифру

print("Обратное число равно:", n2)
