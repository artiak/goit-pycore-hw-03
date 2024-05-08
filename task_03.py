import re


def normalize_phone(phone_number: str) -> str:
    sub_pattern = r"[^\d\+]"
    sub_result = re.sub(sub_pattern, "", phone_number)
    
    return __fix_prefix(sub_result)


def __fix_prefix(phone_number: str) -> str:
    if phone_number.startswith("+380"):
        return phone_number

    if phone_number.startswith("380"):
        return "+" + phone_number

    if phone_number.startswith("0"):
        return "+38" + phone_number


# testing


pns = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

for pn in pns:
    print(normalize_phone(pn))