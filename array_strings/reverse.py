"""
Проблема: Реализуйте функцию для переворота строки (списка символов) на месте

Ограничения
    Можем ли мы предположить, что это строка ASCII?
        да
    Примечание. Строки Unicode могут потребовать специальной обработки в зависимости от вашего языка.
    Поскольку нам нужно сделать это на месте, кажется, мы не можем использовать оператор среза или обратную функцию?
        да
    Поскольку строки Python неизменяемы, можем ли мы вместо этого использовать список символов?
        да
"""
import unittest
from typing import Union


class ReverseString:

    @staticmethod
    def reverse(chars: list) -> Union[list, None]:

        if isinstance(chars, list):

            for i in range(len(chars) // 2):
                chars[i], chars[len(chars) - i - 1] = chars[len(chars) - i - 1], chars[i]

            return chars


class TestReverse(unittest.TestCase):

    def setUp(self) -> None:
        self.func = ReverseString().reverse

    def test_reverse(self):
        self.assertEqual(self.func(None), None)
        self.assertEqual(self.func(['']), [''])
        self.assertEqual(
            self.func(['f', 'o', 'o', ' ', 'b', 'a', 'r']), ['r', 'a', 'b', ' ', 'o', 'o', 'f']
        )
        print('Success: test_reverse')

    def test_reverse_inplace(self):
        target_list = ['f', 'o', 'o', ' ', 'b', 'a', 'r']
        self.func(target_list)
        self.assertEqual(target_list, ['r', 'a', 'b', ' ', 'o', 'o', 'f'])
        print('Success: test_reverse_inplace')


if __name__ == '__main__':
    unittest.main()
