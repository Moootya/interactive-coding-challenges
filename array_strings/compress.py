"""
Проблема: сжать строку так, чтобы «AAABCCDDDD» превратилось в «A3BC2D4».
Сжимайте строку только в том случае, если это экономит место.

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
from typing import Union


class CompressString:

    @staticmethod
    def compress(string: str) -> Union[str, None]:

        if not isinstance(string, str):
            return None

        if len(string) in (0, 1, 2):
            return string

        result = ""
        current_char = string[0]
        count_current_char = 0

        for char in string:

            if char == current_char:
                count_current_char += 1

            else:
                count_current_char = count_current_char if count_current_char > 1 else ""
                result += f"{current_char}{count_current_char}"

                count_current_char = 1
                current_char = char

        count_current_char = count_current_char if count_current_char > 1 else ""
        result += f"{current_char}{count_current_char}"

        if len(result) < len(string):
            return result
        return string


class TestCompress(unittest.TestCase):

    def setUp(self) -> None:
        self.func = CompressString().compress

    def test_compress(self):
        self.assertEqual(self.func(None), None)
        self.assertEqual(self.func(''), '')
        self.assertEqual(self.func('AABBCC'), 'AABBCC')
        self.assertEqual(self.func('AAABCCDDDDE'), 'A3BC2D4E')
        self.assertEqual(self.func('BAAACCDDDD'), 'BA3C2D4')
        self.assertEqual(self.func('AAABAACCDDDD'), 'A3BA2C2D4')
        print('Success: test_compress')


if __name__ == '__main__':
    unittest.main()
