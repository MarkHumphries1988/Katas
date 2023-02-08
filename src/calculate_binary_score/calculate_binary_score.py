from src.count_bits.count_bits import count_bits


def calculate_binary_score(list):
    total = 0

    for number in list:
        if number % 2 == 0:
            total += count_even_bits(number)
            print(bin(number))
            print(count_even_bits(number))
        else:
            total -= count_bits(number)
            print(bin(number))
            print(count_bits(number))

    if total == 0:
        return "tie"
    elif total < 0:
        return "odds win"
    else:
        return "evens win"

    pass


def count_even_bits(integer):
    binary = str(bin(integer))[2:]
    count = 0
    for digit in binary:
        if digit == "0":
            count += 1
    return count
