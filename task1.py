# Напишіть програму, яка запитує у користувача число і обчислює його факторіал. 
# Обробіть виняток, що виникає при введенні від'ємного числа, і виведіть повідомлення про помилку.



def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)
    
try:
    number = int(input("Enter number: "))
    
    if number < 0:
        raise ValueError("You entered a number less than zero")
    else:
        print(factorial(number))   
except ValueError as e:
    print(e) 
    
