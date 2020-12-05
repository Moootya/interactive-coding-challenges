"""
Проблема: определить, является ли строка перестановкой другой строки
— Если символы в одной строке равным символам в другой, то очевидно, что одна строка является перестановкой другой

Ограничения
    Можем ли мы предположить, что это строка ASCII?
        да
    Примечание. Строки Unicode могут потребовать специальной обработки в зависимости от вашего языка.
    Пробелы важны?
        да
    Это чувствительно к регистру? «Перо», «мусорное ведро» - это не совпадение?
        да
    Можем ли мы использовать дополнительные структуры данных?
        да
    Можем ли мы предположить, что это умещается в памяти?
        да
"""
import unittest


class Permutations:

    @staticmethod
    def is_permutation(str1, str2):
        if isinstance(str1, str) and isinstance(str2, str):
            if set(str1) == set(str2) and len(str1) == len(str2):
                return True
        return False


class TestPermutation(unittest.TestCase):

    def setUp(self) -> None:
        self.func = Permutations().is_permutation

    def test_permutation(self):
        self.assertEqual(self.func(None, 'foo'), False)
        self.assertEqual(self.func('', 'foo'), False)
        self.assertEqual(self.func('Nib', 'bin'), False)
        self.assertEqual(self.func('act', 'cat'), True)
        self.assertEqual(self.func('a ct', 'ca t'), True)
        self.assertEqual(self.func('dog', 'doggo'), False)
        print('Success: test_permutation')
