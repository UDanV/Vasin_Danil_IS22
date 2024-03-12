from typing import Pattern
import re

with open("test_string.txt", encoding="utf-8") as f:
    data = f.read()


def get_data(pattern: Pattern[str]) -> str:
    return ' | '.join(pattern.findall(data))


ex_1 = re.compile(r"\d+")
print(f"Все натуральные числа: {get_data(ex_1)}\n")

ex_2 = re.compile(r"[A-ZА-Я]+")
print(f"Все «слова», написанные капсом: {get_data(ex_2)}\n")

ex_3 = re.compile(r"[А-Я][0-9].", re.I)
print(f"Все слова, в которых есть русская буква, а за ней цифра: {get_data(ex_3)}\n")

ex_4 = re.compile(r"\b[А-ЯA-ZЁ]\w+")
print(f"Все слова, начинающиеся с русской или латинской большой букв: {get_data(ex_4)}\n")

ex_5 = re.compile(r"\b[АЕЁИОУЫЭЮЯaeiou]\w+", re.I)
print(f"Все слова, которые начинаются на гласную: {get_data(ex_5)}\n")

ex_6 = re.compile(r"\b[а-яA-Z]+\d{2,}[а-яA-Z]+", re.I)
print(f"Все натуральные числа, не находящиеся на границе слова: {get_data(ex_6)}\n")

ex_7 = re.compile(r"\S*\*\S", re.DOTALL)
print(f"Найдите строчки, в которых есть символ * (. — это точно не конец строки!): {get_data(ex_7)}\n")

ex_8 = re.compile(r"\(.*?\)+", re.DOTALL)
print(f"Найдите строчки, в которых есть открывающая и когда-нибудь потом закрывающая скобки: {get_data(ex_8)}\n")

ex_9 = re.compile(r'<a href="#\d+">.*</a>', re.DOTALL)
print(f"Выделите одним махом весь кусок оглавления (в конце примера, вместе с тегами): \n{get_data(ex_9)}\n")

ex_10 = re.compile(r'<a href="#\d+">(.*?)</a>', re.DOTALL)
print(f"Выделите одним махом только текстовую часть оглавления, без тегов: {get_data(ex_10)}\n")

ex_11 = re.compile(r"^\s*$", re.MULTILINE)
print(f"Найдите пустые строчки: {get_data(ex_11)}\n")

ex_12 = re.compile(r'(<a href="#\d+">).*?(</a>)')
print("Все теги, не включая их содержимое: ")
[print(f"{tags}") for tags in map(lambda x: " ".join(x), ex_12.findall(data))]
