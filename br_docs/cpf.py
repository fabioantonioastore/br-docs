from typing import Annotated

from pydantic import AfterValidator


def is_masked(cpf: str) -> bool:
    return "." in cpf and "-" in cpf


def mask(cpf: str) -> str:
    if is_masked(cpf):
        return cpf
    new_cpf = ""
    digit_position = 0
    for digit in cpf:
        digit_position += 1
        if digit_position == 3 or digit_position == 6:
            new_cpf += digit + "."
            continue
        if digit_position == 9:
            new_cpf += digit + "-"
            continue
        new_cpf += digit
    return new_cpf


def remove_mask(cpf: str) -> str:
    if not is_masked(cpf):
        return cpf
    new_cpf = ""
    for digit in cpf:
        if digit.isnumeric():
            new_cpf += digit
    return new_cpf


def __is_first_verificator_digit_valid(cpf: str) -> bool:
    result = 0
    sequence = 10
    for digit in cpf[:-2:]:
        result += int(digit) * sequence
        sequence -= 1
    result = (result * 10) % 11
    if result == 10:
        result = 0
    return str(result) == cpf[-2]


def is_first_verificator_digit_valid(cpf: str) -> bool:
    cpf = remove_mask(cpf)
    return __is_first_verificator_digit_valid(cpf)


def validate_first_verificator_digit(cpf: str) -> str:
    if not is_first_verificator_digit_valid(cpf):
        raise "Invalid first verificator digit"
    return cpf


def __is_second_verificator_digit_valid(cpf: str) -> bool:
    sequence = 11
    result = 0
    for digit in cpf[:-1:]:
        result += int(digit) * sequence
        sequence -= 1
    result = (result * 10) % 11
    if result == 10:
        result = 0
    return str(result) == cpf[-1]


def is_second_verificator_digit_valid(cpf: str) -> bool:
    cpf = remove_mask(cpf)
    return __is_second_verificator_digit_valid(cpf)


def validate_second_verificator_digit(cpf: str) -> str:
    if not is_second_verificator_digit_valid(cpf):
        raise "Invalid second verificator digit"
    return cpf


def __is_valid(cpf: str) -> bool:
    if len(cpf) != 11 or cpf.count(cpf[0]) == 11:
        return False
    return __is_first_verificator_digit_valid(
        cpf
    ) and __is_second_verificator_digit_valid(cpf)


def is_valid(cpf: str) -> bool:
    cpf = remove_mask(cpf)
    return __is_valid(cpf)


def validate(cpf: str) -> str:
    cpf = remove_mask(cpf)
    if not __is_valid(cpf):
        raise "Invalid CPF"
    return cpf


def generate() -> str:
    pass


CPF = Annotated[str, AfterValidator(validate)]
