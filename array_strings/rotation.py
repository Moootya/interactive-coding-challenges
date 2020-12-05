"""
Проблема: определить, является ли строка s1 вращением другой строки s2, вызвав (только один раз) функцию is_substring

Ограничения
    Можем ли мы предположить, что это строка ASCII?
        да
    Примечание. Строки Unicode могут потребовать специальной обработки в зависимости от вашего языка.
    Это чувствительно к регистру?
        да
    Можем ли мы использовать дополнительные структуры данных?
        да
    Можем ли мы предположить, что это умещается в памяти?
        да
"""
import unittest


class Rotation:

    @staticmethod
    def is_substring(s1, s2):
        return s1 in s2

    def is_rotation(self, s1, s2) -> bool:

        if not isinstance(s1, str) or not isinstance(s2, str):
            return False

        if len(s1) != len(s2):
            return False

        return self.is_substring(s1, s2 + s2)


class TestRotation(unittest.TestCase):

    def setUp(self) -> None:
        self.func = Rotation().is_rotation

    def test_rotation(self):
        self.assertEqual(self.func('o', 'oo'), False)
        self.assertEqual(self.func(None, 'foo'), False)
        self.assertEqual(self.func('', 'foo'), False)
        self.assertEqual(self.func('', ''), True)
        self.assertEqual(self.func('foobarbaz', 'barbazfoo'), True)
        self.assertEqual(self.func('1234', '2341'), True)
        print('Success: test_rotation')


if __name__ == '__main__':
    unittest.main()
