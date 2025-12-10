import re
from datetime import datetime  # Исправлено: импортируем конкретный класс datetime

from src.masks import mask_account_number, mask_card_number


def mask_account_card(input_string: str) -> str:  # Исправлен синтаксис аннотации
    """
    Маскирует номер банковской карты или счета в зависимости от входной строки.

    Принимает строку формата "Visa Platinum 7000792289606361" или
    "Счет 73654108430135874305".
    Определяет тип (карта или счет) и замаскировывает номер, используя
    функции из модуля `masks`.

    Args:
        input_string: Строка, содержащая тип и номер карты/счета.

    Returns:
        Строка с замаскированным номером.

    Raises:
        ValueError: Если не удалось извлечь номер из строки или номер недействителен
                    (например, не 16 цифр для карты или не 20 для счета).

    Примеры:
        Visa Platinum 7000792289606361 -> Visa Platinum 7000 79** **** 6361
        Счет 73654108430135874305 -> Счет **4305
    """
    # Ищем последовательность цифр в конце строки
    match = re.search(r'(\d+)$', input_string)
    if not match:
        raise ValueError("Входная строка не содержит номера карты или счета.")

    number = match.group(1)  # Извлекаем сам номер
    name = input_string[:match.start()].strip()  # Извлекаем название, обрезая пробелы

    # Теперь используем функции маскировки из src.masks
    # Они уже содержат проверки на корректность длины и то, что это цифры
    if "Счет" in name:
        masked_number = mask_account_number(number)
    else:  # Предполагаем, что все остальное - это карты
        masked_number = mask_card_number(number)

    return f"{name} {masked_number}"


def get_date(date_string: str) -> str:  # Исправлен синтаксис аннотации
    """
    Преобразует строку даты из формата "YYYY-MM-DDTHH:MM:SS.microseconds"
    в формат "ДД.ММ.ГГГГ".

    Принимает строку с датой и временем, например "2024-03-11T02:26:18.671407".

    Args:
        date_string: Строка даты и времени в формате ISO 8601
                     ("YYYY-MM-DDTHH:MM:SS.ffffff").

    Returns:
        Строка с датой в формате "ДД.ММ.ГГГГ".

    Raises:
        ValueError: Если формат входной строки не соответствует ожидаемому формату даты.

    Пример:
        "2024-03-11T02:26:18.671407" -> "11.03.2024"
    """
    try:
        # Парсим строку в объект datetime
        # Используем fromisoformat, так как это более надежный способ для ISO 8601
        dt_object = datetime.fromisoformat(date_string)
        # Форматируем объект datetime в нужный строковый формат
        return dt_object.strftime("%d.%m.%Y")
    except ValueError:
        raise ValueError(
            "Некорректный формат даты. Ожидается 'YYYY-MM-DDTHH:MM:SS.ffffff'"
        )
