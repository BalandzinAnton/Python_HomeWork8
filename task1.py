# 1)
# Написать программу, где создадим класс Soup (для определения типа супа), принимающий
# 1 аргумент - который отвечает за основной продукт к выбираемому супу.
# В этом классе создать метод show_my_soup(), выводящий на печать «Суп - {Основной продукт}»
# в случае наличия добавки
# Это как доп к этой задаче - иначе отобразится следующая фраза: «Обычный кипяток»

class Soup():
    def __init__(self, soup_ingredient):
        self.soup_ingredient = soup_ingredient

    def show_my_soup(self):
        types_of_soup = {"капуста": "щи", "комбу": "даси", "говядина": "харчо", "фарш": "тако"}
        my_soup = types_of_soup.get(self.soup_ingredient.lower())
        if my_soup == None:
            print("Обычный кипяток")
        else:
            print(f"Суп - {my_soup}, ингридиент - {self.soup_ingredient}")

soup = Soup("Говядина")
soup.show_my_soup()
