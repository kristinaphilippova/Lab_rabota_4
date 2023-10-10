def convert_to_words(number):
    ones = ['', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять']
    teens = ['десять', 'одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать',
             'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
    tens = ['', '', 'двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
    hundreds = ['', 'сто', 'двести', 'триста', 'четыреста', 'пятьсот', 'шестьсот', 'семьсот', 'восемьсот', 'девятьсот']
    thousands = ['', 'тысяча', 'тысячи', 'тысяч']
    
    # Проверка введенного числа
    if not 1 <= number <= 100000:
        return "Введенное число не входит в диапазон от 1 до 100000"
    
    # Функция для преобразования двух последних цифр числа
    def convert_last_two_digits(num):
        if num < 10:
            return ones[num]
        elif num < 20:
            return teens[num-10]
        else:
            tens_digit = num // 10
            ones_digit = num % 10
            return tens[tens_digit] + ' ' + ones[ones_digit]
    
    # Преобразование числа в словесное представление
    if number == 0:
        word = 'ноль'
    else:
        word = ''
        # Обработка тысяч
        if number >= 1000:
            thousands_digit = number // 1000
            if thousands_digit == 1:
                word += 'одна '
            elif thousands_digit == 2:
                word += 'две '
            else:
                word += convert_last_two_digits(thousands_digit) + ' '
            word += thousands[get_thousands_index(thousands_digit)] + ' '
            number %= 1000
        
        # Обработка сотен
        if number >= 100:
            hundreds_digit = number // 100
            word += hundreds[hundreds_digit] + ' '
            number %= 100
        
        # Обработка десятков и единиц
        if number >= 20:
            tens_digit = number // 10
            word += tens[tens_digit] + ' '
            number %= 10
        word += convert_last_two_digits(number)
    
    # Вывод словесного представления суммы с правильным окончанием валюты
    if word.endswith('один'):
        word += ' рубль'
    elif word.endswith('два') or word.endswith('три') or word.endswith('четыре'):
        word += ' рубля'
    else:
        word += ' рублей'
    
    # Первое слово с большой буквы
    word = word.capitalize()
    
    return word


def get_thousands_index(num):
    if 5 <= num % 100 <= 20 or num % 10 >= 5 or num % 10 == 0:
        return 3
    elif 2 <= num % 10 <= 4:
        return 2
    else:
        return 1


# Получение ввода от пользователя и вызов функции для преобразования числа в слова
try:
    number = int(input("Введите число от 1 до 100000: "))
    result = convert_to_words(number)
    print(result)
except ValueError:
    print("Ошибка! Введите корректное число.")
