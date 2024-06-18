def filter_by_state(operations: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """функцию, которая принимает на вход список словарей
     и значение для ключа state(опциональный параметр со значением по умолчанию EXECUTED)
      и возвращает новый список,
     содержащий только те словари,
      у которых ключ state содержит переданное в функцию значение.
      """
    return [
        operation
        for operation in operations
        if operation['state'] == state
    ]


def sort_by_date(operations: list[dict], is_reverse: bool = True) -> list[dict]:
    """функцию, которая принимает на вход список словарей и возвращает новый список,
     в котором исходные словари отсортированы по убыванию даты (ключ date.
 Функция принимает два аргумента, второй необязательный задает порядок сортировки (убывание, возрастание).
    """
    return [
        operation
        for operation in sorted(operations, key=lambda x: x['date'], reverse=is_reverse)
    ]
