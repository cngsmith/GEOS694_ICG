# Reformatted code by Celine according to PEP-8 standards

import random
import time

random_num = 20
num_calc = 5
seconds = 1

def calc_stuff(x, y, z):
    if x > y:
        result = x * y + z
    else:
        result = y * z - x
    return result

def print_data(data_list):
    for i in range(0, len(data_list)):
        print("Index:", i, "Value:", data_list[i])

def generate_numbers(n):
    numbers=[]
    for i in range(n):
        numbers.append(random.randint(1, 100))
    return numbers

def average(nums):
    total = 0
    for n in nums:
        total += n
    if len(nums) == 0:
        return 0
    return total / len(nums)

def process(nums):
    processed=[]
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            processed.append(nums[i] * 2)
        else:
            processed.append(nums[i] + 1)
    return processed


def main():
    print("Starting program:")

    nums = generate_numbers(random_num)
    print_data(nums)
    avg = average(nums)

    print("Average is:", avg)

    processed = process(nums)

    print("Processed values:")

    print_data(processed)

    for i in range(num_calc):
        value = calc_stuff(i, avg, processed[i])
        print("Calc", i, value)
    t = time.time()
    while time.time() - t < seconds:
        pass
    print("Done")

if __name__=="__main__":
    main()