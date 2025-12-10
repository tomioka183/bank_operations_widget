"""
Модуль для маскировки номеров карт и счетов.
"""


def mask_card_number(card_number: str) -> str:
    """
    Маскирует номер банковской карты, оставляя открытыми первые 6 и последние 4 цифры.
    Пример: "7000792289606361" -> "7000 79** **** 6361"

    Args:
        card_number: Номер банковской карты в виде строки (должен содержать 16 цифр).

    Returns:
        Замаскированная строка номера карты.

    Raises:
        ValueError: Если номер карты не является 16-значным числом или не число.
    """
    if not (card_number.isdigit() and len(card_number) == 16):
        raise ValueError("Номер карты должен содержать 16 цифр.")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def mask_account_number(account_number: str) -> str:
    """
    Маскирует номер банковского счета, оставляя открытыми только последние 4 цифры.
    Пример: "73654108430135874305" -> "**4305"
    Args:
        account_number: Номер банковского счета в виде строки (должен содержать 20 цифр).
    Returns:
        Замаскированная строка номера счета.
    Raises:
        ValueError: Если номер счета не является 20-значным числом или не число.
    """
    if not (account_number.isdigit() and len(account_number) == 20):
        raise ValueError("Номер счета должен содержать 20 цифр.")
    return f"**{account_number[-4:]}"


if __name__ == "__main__":
    print("--- Проверка mask_card_number ---")
    print(f"'7000792289606361' -> {mask_card_number('7000792289606361')}")
    print(f"'1596837868705199' -> {mask_card_number('1596837868705199')}")
    try:
        mask_card_number('123')
    except ValueError as e:
        print(f"Ошибка (как ожидалось): {e}")
    print("\n--- Проверка mask_account_number ---")
    print(f"'73654108430135874305' -> {mask_account_number('73654108430135874305')}")
    print(f"'64686473678894779589' -> {mask_account_number('64686473678894779589')}")
    try:
        mask_account_number('123')
    except ValueError as e:
        print(f"Ошибка (как ожидалось): {e}")
    try:
        mask_account_number('abc')
    except ValueError as e:
        print(f"Ошибка (как ожидалось): {e}")
