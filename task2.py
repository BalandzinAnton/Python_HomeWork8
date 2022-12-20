# 2)
# Нужно напистаь программу
# В ней используем классы - имя студента name, номер группы group и список полученных оценок progress.
# В самой программе вводим список всех студентов.
# В программе нужно вывести список студентов, отсортированный по имени, А так же студентов,
# у которых низкие оценки

from statistics import mean

class Name():
    def names_of_the_students(self):
        self.names = ["Петров", "Сидоров", "Иванов", "Некифоров", "Пупкин"]
        self.names.sort()
        print(self.names)
class Group():
    def number_of_group(self):
        self.numberOfGroup = "12-F"
        print(f"Успеваемость группы №{self.numberOfGroup}")
class Progress():
     def progress_students(self):
         self.petrov = [9, 8, 7, 9, 2, 10, 7]
         self.sidorov = [3, 2, 3, 7, 5, 5]
         self.ivanov = [9, 2, 5, 7]
         self.nekiforov = [9, 2, 10, 7]
         self.pupkin = [2, 2, 4, 7]
         self.petrov_sr = round(mean(self.petrov), 2)
         self.sidorov_sr = round(mean(self.sidorov), 2)
         self.ivanov_sr = round(mean(self.ivanov), 2)
         self.nekiforov_sr = round(mean(self.nekiforov), 2)
         self.pupkin_sr = round(mean(self.pupkin), 2)
         self.spisok = {"Петров": self.petrov_sr, "Сидоров": self.sidorov_sr,
                   "Иванов": self.ivanov_sr, "Некифоров": self.nekiforov_sr,
                   "Пупкин": self.pupkin_sr}
         print(self.spisok)
         print('Низкая успеваемость (ниже 6 баллов) у следующих учеников:')
         for k, v in self.spisok.items():
             if v < 6:
                 print(k, v)

numbers = Group()
numbers.number_of_group()

names = Name()
names.names_of_the_students()

progress = Progress()
progress.progress_students()