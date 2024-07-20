# 1. Преобразуем строку в нижний регистр
# 2. Удаляем пробелы и символы пунктуации
# 3. Определяем длину строки
# 4. Перебираем строку до половины её длины, сравнивая соответствующие символы с начала и конца строки
# 5. Если встретилось несовпадение, завершаем функцию, возвращая false
# 6. Если несовпадение не встретилось, по окончании цикла возвращаем true


def is_palindrome(some_string):
    processed_string = some_string.lower()
    processed_string = ''.join(char for char in processed_string if char.isalnum())
    length = len(processed_string)

    for i in range(length // 2):
        if processed_string[i] != processed_string[length - 1 - i]:
            # В данном учебном примере будем возвращать не True/False, а сообщение
            return f"{some_string.ljust(55)} – не является палиндромом"
    return f"{some_string.ljust(55)} – является палиндромом"


print(is_palindrome("Эта строка не является палиндромом"))
print(is_palindrome("Утро поползло по порту"))
print(is_palindrome("Дорого небо, да надобен огород"))
print(is_palindrome("Ешь немытого ты меньше!"))
print()
print(is_palindrome("Эта строка тоже не является палиндромом"))
print(is_palindrome("Мама дала ситро, торт и сала дамам???"))
print(is_palindrome("У дезертира жена не жарит резеду!!!"))
print(is_palindrome("Я радую тётю, дядю ударя! Я радую дядю, тётю ударя!"))
