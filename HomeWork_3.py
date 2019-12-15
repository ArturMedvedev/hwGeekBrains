'''
Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход). Последний атрибут должен быть защищенным
и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
'''


class Worker:  # Создаем класс
    # Определяем атрибуты
    name = 'Aya'
    surname = 'Bree'
    position = 'M.I.S.T. agent'
    _income = {'wage': 5000, 'bonus': 3000}


class Position(Worker):  # Создаем дочерний класс

    def get_full_name(self):  # Метод получения полного имени
        return f'{self.name} {self.surname}'

    def get_total_income(self):  # Метод получения дохода с учетом премии
        result = 0
        for itm in self._income.values():
            result += int(itm)
        return result


position_1 = Position()  # Создаем экземпляр класса
# Проверяем значения атрибутов
print(position_1.name)
print(position_1.surname)
print(position_1.position)
print(position_1._income)

print(position_1.get_full_name())  # Вызываем метод получения полного имени
print(position_1.get_total_income())  # Вызываем метод получения полного дохода
