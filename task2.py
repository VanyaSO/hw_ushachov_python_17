# Реалізуйте перше завдання через функцію. Функція повинна приймати число як параметр і повертати його факторіал. 
# Перевірка коректності отриманих даних повинна бути всередині функції. Створіть дві версії реалізації функції:

# Перша версія не обробляє виняток усередині функції. Уся обробка знаходиться зовні;
# Друга версія обробляє виняток усередині функції

number = int(input("Enter number: "))

def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)
    
try:
    if number < 0:
        raise ValueError("You entered a number less than zero")
    else:
        print(factorial(number))   
except ValueError as e:
    print(e) 
    
    
def factorial2(number):
    if number == 0 or number == 1:
        return 1
    
    try:
        if number < 0:
            raise ValueError("You entered a number less than zero")
        else:
            return print(number * factorial(number - 1))
    except ValueError as e:
        print(e) 
        
factorial2(number)