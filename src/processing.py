from typing import List, Dict, Any

def filter_by_state(transactions: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    """
    Фильтрует список банковских операций по статусу.

    Функция принимает на вход список словарей, представляющих банковские операции,
    и опциональный параметр `state`, который по умолчанию равен 'EXECUTED'.
    Возвращает новый список, содержащий только те словари (операции),
    у которых ключ 'state' содержит переданное в функцию значение.

    :param transactions: Список словарей, где каждый словарь представляет одну банковскую операцию.
    :param state: Строка, обозначающая статус операции (например, 'EXECUTED', 'CANCELED', 'PENDING').
                  По умолчанию 'EXECUTED'.
    :return: Новый список словарей, содержащий только операции с указанным статусом.
             Если ключ 'state' отсутствует в словаре, эта операция игнорируется.
    """
    filtered_transactions: List[Dict[str, Any]] = [
        transaction for transaction in transactions
        if transaction.get('state') == state
    ]
    return filtered_transactions

if __name__ == "__main__":
    operations_data = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364', 'operationAmount': {'amount': '8221.72', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'VISA Platinum 7000 7922 8960 6361', 'to': 'Счет 9600 7731 5462 7267'},
        {'id': 59422949, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241670', 'operationAmount': {'amount': '14591.07', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Visa Platinum 5109 0100 0019 9673', 'to': 'Счет 5071 9240 0005 8475'},
        {'id': 61506461, 'state': 'EXECUTED', 'date': '2018-10-25T02:04:09.680665', 'operationAmount': {'amount': '50000.00', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Открытие вклада', 'to': 'Счет 4142 4586 7541 4070'},
        {'id': 50000000, 'state': 'PENDING', 'date': '2020-01-01T12:00:00.000000', 'operationAmount': {'amount': '100.00', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Тестовая операция', 'to': 'Счет 1234 5678 9012 3456'},
        {'id': 70000000, 'date': '2021-01-01T12:00:00.000000', 'description': 'Операция без статуса'} # Пример словаря без ключа 'state'
    ]

    print("--- Testing filter_by_state ---")

    # Вызов с состоянием по умолчанию 'EXECUTED'
    executed_ops = filter_by_state(operations_data)
    print("\nEXECUTED operations:")
    for op in executed_ops:
        print(op)

    # Вызов с состоянием 'CANCELED'
    canceled_ops = filter_by_state(operations_data, state='CANCELED')
    print("\nCANCELED operations:")
    for op in canceled_ops:
        print(op)

    # Вызов с состоянием 'PENDING'
    pending_ops = filter_by_state(operations_data, state='PENDING')
    print("\nPENDING operations:")
    for op in pending_ops:
        print(op)

    # Вызов с несуществующим состоянием
    non_existent_ops = filter_by_state(operations_data, state='NON_EXISTENT')
    print("\nNON_EXISTENT operations:")
    for op in non_existent_ops:
        print(op)