# class BinarySearch:
#     def __init__(self, array: list):
#         self.arr = array
#         self.arr.sort()
#         self.desired_num = int(input('enter the number u want to find:'))
#
#     def search(self):
#         low = 0
#         high = len(self.arr) - 1
#         print(self.arr)
#
#         while low <= high:
#             mid = (low + high) // 2
#
#             if self.arr[mid] == self.desired_num:
#                 return f'Index: {mid}'
#             elif self.arr[mid] > self.desired_num:
#                 high = mid - 1
#             elif self.arr[mid] < self.desired_num:
#                 low = mid + 1
#         return f'No Value'
#
#
# nums = [64, 23, 89, 6, 1, 12, 33]
# bin_search = BinarySearch(nums)
# print(bin_search.search())

## class Quick:
#     def __init__(self, arr):
#         self.arr = arr
#
#     def partition(self, array):
#         if len(array) <= 1:
#             return array
#         element = array[0]
#         left = list(filter(lambda nums: nums < element, array))
#         center = [nums for nums in array if nums == element]
#         right = list(filter(lambda nums: nums > element, array))
#
#         return self.partition(left) + center + self.partition(right)
#
#     def quick_sort(self):
#         if len(self.arr) <= 1:
#             return self.arr
#         else:
#             element = self.arr[0]
#             left = list(filter(lambda nums: nums < element, self.arr))
#             center = [nums for nums in self.arr if nums == element]
#             right = list(filter(lambda nums: nums > element, self.arr))
#
#         return self.partition(left) + center + self.partition(right)
#
#
# arr_nums = [64, 23, 89, 6, 1, 12, 33]
# print(arr_nums)
# quick = Quick(arr_nums)
# print(quick.quick_sort())

# class Bubble():
#     def __init__(self, buble):
#         self.bub = buble
#
#     def bubble_sort(self):
#         swapped = False
#         for number_1 in range(len(array) - 1, 0, -1):
#             for number_2 in range(number_1):
#                 if array[number_2] > array[number_2 + 1]:
#                     array[number_2], array[number_2 + 1] = array[number_2 + 1], array[number_2]
#                     swapped = True
#             if swapped:
#                 swapped = False
#             else:
#                 break
#         return array
#
# array = [64, 23, 89, 6, 1, 12, 33]

# print(Bubble.bubble_sort(array))
class Palindrome:
    def __init__(self, number: int):
        self.num = number

    def is_palindrome_short(self):
        if self.num <= 0 or str(self.num) != str(self.num)[::-1]:
            return False
        else:
            return True

    def is_palindrome_str(self):
        if self.num <= 0:
            return False
        n = 1
        for i in range(len(str(self.num))):
            if str(self.num)[i] != str(self.num)[len(str(self.num)) - n]:
                return False
            n += 1
        return True


num = 342
num_1 = Palindrome(num)
print(f'{num}: {num_1.is_palindrome_short()}')
print(f'{num}: {num_1.is_palindrome_str()}')
