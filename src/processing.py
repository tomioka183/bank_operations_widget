import datetime
from typing import List, Dict, Any


def filter_operations_by_status(
    operations: List[Dict[str, Any]], status: str
) -> List[Dict[str, Any]]:
    """
    Фильтрует список финансовых операций по их статусу.

    Args:
        operations: Список словарей, где каждый словарь представляет
                    финансовую операцию и должен содержать ключ 'state'.
        status: Статус, по которому необходимо отфильтровать операции
                (например, 'EXECUTED', 'PENDING').

    Returns:
        Новый список операций, содержащий только те, что имеют указанный статус.
    """
    filtered_operations = [operation for operation in operations if operation.get('state') == status]
    return filtered_operations


def sort_operations_by_date(
    operations: List[Dict[str, Any]], ascending: bool = True
) -> List[Dict[str, Any]]:
    """
    Сортирует список финансовых операций по дате.

    Args:
        operations: Список словарей, где каждый словарь представляет
                    финансовую операцию и должен содержать ключ 'date'
                    с датой в формате ISO 8601 (например, "2023-11-20T10:00:00").
        ascending: Булево значение, определяющее порядок сортировки.
                   Если True (по умолчанию), сортировка происходит от старых
                   дат к новым. Если False, от новых к старым.

    Returns:
        Новый список операций, отсортированный по дате.
    """
    # Создаём копию списка, чтобы не изменять исходный
    sorted_operations = sorted(
        operations,
        key=lambda operation: datetime.datetime.fromisoformat(operation['date'].replace('Z', '+00:00')),
        reverse=not ascending
    )
    return sorted_operations


if __name__ == "__main__":
    sample_operations = [
        {"id": 1, "state": "EXECUTED", "date": "2023-11-20T10:00:00", "description": "Оплата"},
        {"id": 2, "state": "PENDING", "date": "2023-11-19T15:30:00", "description": "Перевод"},
        {"id": 3, "state": "EXECUTED", "date": "2023-11-21T09:15:00", "description": "Покупка"},
        {"id": 4, "state": "CANCELED", "date": "2023-11-18T12:00:00", "description": "Отмена"},
    ]

    print("Исходные операции:")
    for op in sample_operations:
        print(op)

    print("\nОтфильтрованные по статусу 'EXECUTED':")
    filtered = filter_operations_by_status(sample_operations, "EXECUTED")
    for op in filtered:
        print(op)

    print("\nОтсортированные по дате (от старых к новым):")
    sorted_asc = sort_operations_by_date(sample_operations)
    for op in sorted_asc:
        print(op)

    print("\nОтсортированные по дате (от новых к старым):")
    sorted_desc = sort_operations_by_date(sample_operations, ascending=False)
    for op in sorted_desc:
        print(op)
