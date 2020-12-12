"""
Проблема: внедрить Fizz Buzz.

Ограничения:
    Что такое шипучка?
        Вернуть строковое представление чисел от 1 до n
        Кратное 3 -> 'Fizz'
        Кратное 5 -> 'Buzz'
        Кратное 3 и 5 -> 'FizzBuzz'
    Можно ли предположить, что введенные данные действительны?
        Нет
    Можем ли мы предположить, что это соответствует памяти?
        да
"""
import unittest


class Solution:

    @staticmethod
    def fizz_buzz(num):

        if num is None:
            raise TypeError

        if num <= 0:
            raise ValueError

        result = []
        for i in range(1, num + 1):

            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")

            elif i % 3 == 0:
                result.append("Fizz")

            elif i % 5 == 0:
                result.append("Buzz")

            else:
                result.append(str(i))

        return result


class TestFizzBuzz(unittest.TestCase):

    def test_fizz_buzz(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.fizz_buzz, None)
        self.assertRaises(ValueError, solution.fizz_buzz, 0)
        expected = [
            '1',
            '2',
            'Fizz',
            '4',
            'Buzz',
            'Fizz',
            '7',
            '8',
            'Fizz',
            'Buzz',
            '11',
            'Fizz',
            '13',
            '14',
            'FizzBuzz'
        ]
        self.assertEqual(solution.fizz_buzz(15), expected)
        print('Success: test_fizz_buzz')


def main():
    test = TestFizzBuzz()
    test.test_fizz_buzz()


if __name__ == '__main__':
    main()
