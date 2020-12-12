"""
Проблема: для массива найдите два индекса, которые в сумме дают определенное значение.
Ограничения:
    Есть одно решение?
        да
    Всегда ли есть решение?
        да
    Является ли массив массивом целых чисел?
        да
    Массив отсортирован?
        Нет
    Возможны ли отрицательные значения?
        да
    Можно ли предположить, что введенные данные действительны?
        Нет
    Можем ли мы предположить, что это соответствует памяти?
        да
"""
import unittest


class Solution:

    # O(len(nums)^2)
    @staticmethod
    def two_sum(nums, val):

        if nums is None or val is None:
            raise TypeError

        if len(nums) == 0 or val == 0:
            raise ValueError

        index_i = 0
        index_j = 0

        for i in range(len(nums)):
            for j in range(len(nums)):

                if nums[i] + nums[j] == val:

                    index_i = i
                    index_j = j

        return sorted([index_i, index_j])

    # O(len(nums))
    @staticmethod
    def optimized_two_sum(nums, val):
        if nums is None or val is None:
            raise TypeError

        if len(nums) == 0 or val == 0:
            raise ValueError

        cache = {}

        for index, num in enumerate(nums):

            target = val - num
            if num in cache:
                return sorted([cache[num], index])
            cache[target] = index


class TestTwoSum(unittest.TestCase):

    def test_two_sum(self):
        solution = Solution()
        self.assertRaises(TypeError, solution.two_sum, None, None)
        self.assertRaises(ValueError, solution.two_sum, [], 0)
        target = 7
        nums = [1, 3, 2, -7, 5]
        expected = [2, 4]
        self.assertEqual(solution.two_sum(nums, target), expected)
        print('Success: test_two_sum')


def main():
    test = TestTwoSum()
    test.test_two_sum()


if __name__ == '__main__':
    main()
