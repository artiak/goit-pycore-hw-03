import random

MIN_VAL: int = 1
MAX_VAL: int = 1000
MIN_QUANT_VAL: int = 0


def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    if (not is_valid_min(min) or
        not is_valid_max(min, max) or
            not is_valid_quantity(min, max, quantity)):
        return []

    unique_random_nums = set()
    while len(unique_random_nums) < quantity:
        unique_random_nums.add(random.randint(min, max))

    return sorted(unique_random_nums)


def is_valid_min(min: int) -> bool:
    if (min < MIN_VAL):
        print(f"Invalid Minimum, must be >= {MIN_VAL}")
        return False

    if (min > MAX_VAL - 1):
        print(f"Invalid Minimum, must be < {MAX_VAL}")
        return False

    return True


def is_valid_max(min: int, max: int) -> bool:
    if (max < min):
        print(f"Invalid Maximum, must be >= {min}")
        return False

    if (max > MAX_VAL):
        print(f"Invalid Maximum, must be <= {MAX_VAL}")
        return False

    return True


def is_valid_quantity(min: int, max: int, quantity: int) -> bool:
    if (quantity < MIN_QUANT_VAL):
        print(f"Invalid Quantity, must be >= {MIN_QUANT_VAL}")
    
    diff = max - min
    max_quantity = to_max_quantity(diff)
    if (quantity > max_quantity):
        print(f"Invalid Quantity, must be <= {max_quantity}")
        return False

    return True


def to_max_quantity(diff: int) -> int:
    edge_quantity = 0 if diff == 0 else 1
    
    return diff + edge_quantity


# testing


def parse_int(num_str: str) -> int:
    try:
        return int(num_str)
    except ValueError:
        print("Input is not a valid integer")


while True:
    min_str = input("Enter Minimum (integer between 1 and 999): ")
    min_int = parse_int(min_str)

    max_str = input(f"Enter Maximum (integer between {min_int} and 1000): ")
    max_int = parse_int(max_str)

    max_quantiy = to_max_quantity(max_int - min_int)
    quant_str = input(f"Enter Quantity (integer between 0 and {max_quantiy}): ")
    quant_int = parse_int(quant_str)

    ticket_numbers = get_numbers_ticket(min_int, max_int, quant_int)

    print(ticket_numbers)
