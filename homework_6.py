class Algorithm:
    def __init__(self, numbers, desired_sum):
        self.numbers = numbers
        self.desired_sum = desired_sum

    def solution(self):
        for i in range(0, len(self.numbers)):
            for j in range(i + 1, len(self.numbers)):
                if self.numbers[i] + self.numbers[j] == self.desired_sum:
                    return [i, j]
        return 'No such numbers'

    def __str__(self):
        return f'numbers: {self.numbers}\n' \
               f'desired sum: {self.desired_sum}'


nums = [2, 7, 11, 15]

find_index = Algorithm(numbers=nums, desired_sum=9)
print(find_index)
print(find_index.solution())