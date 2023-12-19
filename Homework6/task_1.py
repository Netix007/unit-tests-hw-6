"""Программа для сравнения средних значений двух списков."""


class NumsLists:
    """Класс для сравнения средних значений двух списков."""

    def __init__(self, lst1: list[int | float], lst2: list[int | float]):
        """Инициализирует экземпляр класса двумя списками."""
        self.lst1 = lst1
        self.lst2 = lst2

    def get_lists_averages(self) -> tuple[float, float]:
        """Вычисляет и возвращает средние значения двух списков."""
        avg1 = 0
        if self.lst1:
            avg1 = sum(self.lst1) / len(self.lst1)

        avg2 = 0
        if self.lst2:
            avg2 = sum(self.lst2) / len(self.lst2)

        return avg1, avg2

    def compare_averages(self) -> None:
        """Сравнивает средние значения двух списков и выводит результат."""
        avg1, avg2 = self.get_lists_averages()
        if avg1 > avg2:
            print('Первый список имеет большее среднее значение.')
        elif avg1 < avg2:
            print('Второй список имеет большее среднее значение.')
        else:
            print('Средние значения равны.')
