def sum(numbers):
    if not numbers:
        return 0
    print("Calling sum(%s)" % numbers[1:])
    remaining_sum = sum(numbers[1:])
    print("Returning %d + sum(%s)" % (numbers[0], numbers[1:]))
    return numbers[0] + remaining_sum

print(sum([1,2,3,4,5]))