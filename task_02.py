import random

MIN_VAL: int = 1
MAX_VAL: int = 1000


def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    if (not valid_min(min) or
        not valid_max(min, max) or
            not valid_quantity(min, max, quantity)):
        return []

    unique_random_nums = set()
    while len(unique_random_nums) < quantity:
        unique_random_nums.add(random.randint(min, max))

    return sorted(unique_random_nums)


def valid_min(min: int) -> bool:
    if (min < MIN_VAL):
        print("Invalid Minimum, must be >= 1")
        return False

    if (min > MAX_VAL - 1):
        print("Invalid Minimum, must be <= 999")
        return False

    return True


def valid_max(min: int, max: int) -> bool:
    if (max < min):
        print("Invalid Maximum, must be >= Minimum")
        return False

    if (max > MAX_VAL):
        print("Invalid Maximum, must be <= 1000")
        return False

    return True


def valid_quantity(min: int, max: int, quantity: int) -> bool:
    diff = max - min
    edge_variant_num = 1 if diff == 0 else 2
    if (quantity > max - min + edge_variant_num):
        print("Invalid Quantity, must fit into [Minimum - Maximum] range")
        return False

    return True


# testing
def parse_int(in_num: str) -> int:
    try:
        return int(in_num)
    except ValueError:
        print("Input is not a valid integer")


while True:
    min_str = input("Enter Minimum (integer between 1 and 999): ")
    min_int = parse_int(min_str)

    max_str = input("Enter Maximum (integer between 1 and 1000): ")
    max_int = parse_int(max_str)

    quant_str = input(
        "Enter Quantity (integer to fit between Minimum and Maximum): ")
    quant_int = parse_int(quant_str)

    numbers_ticket = get_numbers_ticket(min_int, max_int, quant_int)

    print(numbers_ticket)
