"""
Проблема: реализовать алгоритм, чтобы определить, есть ли в строке все уникальные символы.

Ограничения
    Можем ли мы предположить, что это строка ASCII?
        да
    Примечание. Строки Unicode могут потребовать специальной обработки в зависимости от вашего языка.
    Можно ли предположить, что здесь учитывается регистр?
        да
    Можем ли мы использовать дополнительные структуры данных?
        да
    Можем ли мы предположить, что это умещается в памяти?
        да
"""
import unittest


class UniqueChars:

    @staticmethod
    def has_unique_chars(string: str) -> bool:
        if isinstance(string, str):
            return len(set(string)) == len(string)
        return False


class TestUniqueChars(unittest.TestCase):

    def setUp(self) -> None:
        self.func = UniqueChars().has_unique_chars

    def test_unique_chars(self):
        self.assertEqual(self.func(None), False)
        self.assertEqual(self.func(''), True)
        self.assertEqual(self.func('foo'), False)
        self.assertEqual(self.func('bar'), True)
        print('Success: test_unique_chars')
