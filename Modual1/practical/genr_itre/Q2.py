# Write a Python program that uses a custom iterator to iterate over a list of integers.

class IntegerIterator:
    def __init__(self, nums):
        self.nums = nums  
        self.index = 0  

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.nums):
            result = self.nums[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration  

numbers = [10, 20, 30, 40, 50]

iterator = IntegerIterator(numbers)


for num in iterator:
    print(num)
