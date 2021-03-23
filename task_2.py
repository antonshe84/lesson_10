"""
2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
проекта — одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм.
 У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
 V и H соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания. Реализовать абстрактные
классы для основных классов проекта и проверить работу декоратора @property.
"""

from abc import ABC, abstractmethod


class Clothes(ABC):
    out = 0

    def __init__(self, s):
        self.s = s

    @property
    @abstractmethod
    def calculation(self):
        pass

    def __add__(self, other):
        Clothes.out += self.calculation + other.calculation
        return Costume(0)

    def __str__(self):
        return f"{Clothes.out}"


class Coat(Clothes):
    @property
    def calculation(self):
        return round(self.s / 6.5) + 0.5


class Costume(Clothes):
    @property
    def calculation(self):
        return round((2 * self.s + 0.3) / 100)


palto_1 = Coat(50)
palto_2 = Coat(48)
kostum_1 = Costume(180)
kostum_2 = Costume(175)
sum_1 = palto_1 + kostum_1
sum_1 += palto_2 + kostum_2
print(f"Всего ткани требуется: {sum_1}")

