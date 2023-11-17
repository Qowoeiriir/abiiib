# # 1
# class Soda:
#     def __init__(self, dobav):
#         self.dobav = dobav
#
#     def dobav_drink(self):
#         if self.dobav:
#             print(f"Газировка и {self.dobav}")
#         else:
#             print("Обычная газировка")
#
#
# # Пример с добавлением сахара
# soda_sugar = Soda("Сахар")
# soda_sugar.dobav_drink()  # Выведет: Газировка и сахар
# # Пример без добавлением сахара
# soda_ordinary = Soda("")
# soda_ordinary.dobav_drink()  # Выведет: Обычная газировка
# 2
# class TriangleChecker:
#     def __init__(self, a, b, c):#Стороны треугольника
#         self.a= a
#         self.b = b
#         self.c = c
#
#     def is_triangle(self):
#         if self.a <= 0 or self.b <= 0 or self.c <= 0:
#             return "С отрицательными числами ничего не выйдет!"
#         if not isinstance(self.a, (int, float)) or not isinstance(self.b, (int, float)) or not isinstance(
#                 self.c, (int, float)):
#             return "Нужно вводить только числа!"
#         if self.a + self.b > self.c and self.a + self.c> self.b and self.b + self.c > self.a:
#             return "Ура, можно построить треугольник!"
#         else:
#             return "Жаль, но из этого треугольник не сделать."
#
#
# triangle1 = TriangleChecker(5, 4, 3)
# print(triangle1.is_triangle())  # Выводит: Ура, можно построить треугольник!
#
# triangle2 = TriangleChecker(-2, 3, 4)
# print(triangle2.is_triangle())  # Выводит: С отрицательными числами ничего не выйдет!
#
# triangle3 = TriangleChecker(1, 2, 3)
# print(triangle3.is_triangle())  # Выводит: Нужно вводить только числа!
#
# triangle4 = TriangleChecker(5, 9, 3)
# print(triangle4.is_triangle())  # Выводит: Жаль, но из этого треугольник не сделать.
# 3
# class Nikola:
#
#     def __init__(self,name,age):
#         self.name = self.priobrozovat(name) #Имя
#         self.age =age #Возраст
#
#     def priobrozovat(self,name):
#         if name != "Николай":
#             return "Я не "+ name + ",а Николай"
#         return name
#
#     def __str__(self):
#         return f"Имя:{self.name}.Возраст:{self.age}"
#
# nikolay = Nikola("Николай",27)#Выведет:Николай .Возраст 24
# print(nikolay)
#
# maxim = Nikola("Максим",24)#Выведет:Я не Максим,а Николай.Возраст 24
# print(maxim)

# 4
#
# class RealString():
#     def __init__(self, text):
#         self.text = text
#
#     def __add__(self, other):
#         return len(self.text) + len(other.text)
#
#     def __lt__(self, other):
#         return len(self.text) < len(other.text)
#
#     def __gt__(self, other):
#         return len(self.text) > len(other.text)
#
#     def __eq__(self, other):
#         return len(self.text) == len(other.text)
#
# text1 = RealString("Apple")
# text2 = RealString("Яблоко")
#
# result = text1 + text2
# print(result) # Выведет 12
#
# result = text1 > text2
# print(result) # Выведет False
#
# result = text1 < text2
# print(result) # Выведет True
#
# result = text1 == text2
# print(result) # Выведет False
#5
def sozdaem_triangle(n):
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        if i >= 2:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle


n = 5 # n = количество строчек
result = sozdaem_triangle(n)
for row in result:
    print(row)

