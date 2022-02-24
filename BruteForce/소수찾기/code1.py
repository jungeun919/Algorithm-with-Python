from itertools import permutations

def is_prime(num):
    if num <= 1:
        return False
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
    return True

def solution(numbers):
    array = []
    
    for i in range(len(numbers)):
        perList = list(permutations(numbers, i + 1))
        numList = [int(''.join(i)) for i in perList]
        for num in numList:
            if is_prime(num):
                array.append(num)

    array = set(array)
    return len(array)