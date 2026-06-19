nums = [34, 56, 76, 68, 37, 84]

all_num = all(isinstance(num, int) for num in nums)
print(all_num)

def greet():
    return "Welcome"
