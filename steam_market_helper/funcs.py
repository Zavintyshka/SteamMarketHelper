import json
from typing import List
from .steam_market_helper_types import Item
from .api_call import make_api_call
from .parser import parse_market_history
from .settings import URL

__all__ = ["dump_item_list_to_json", "get_item_list"]


# Запись
def dump_item_list_to_json(path: str):
    item_list = get_item_list(from_file=False)
    with open(path, "w") as json_file:
        json.dump([*(item._asdict() for item in item_list)], json_file)


# Считывание
def get_item_list(from_file: bool) -> List[Item]:
    if from_file:
        path = input("Введите путь до дампа: ")
        return load_item_list_from_json(path)
    else:
        return load_item_list_from_api(is_log=True, is_test=False)


def load_item_list_from_api(is_log: bool, is_test: bool = True) -> List[Item]:
    full_item_list = []
    market_api_response = make_api_call(URL.format("0"))
    first_item_list = parse_market_history(market_api_response)
    if is_test:
        return first_item_list
    total_items = market_api_response.total_items
    paginator = (start * 10 for start in range(1, (total_items // 10) + 1))
    if is_log:
        print_page("1", item_list=first_item_list)

    for page_num, start in enumerate(paginator, start=2):
        market_api_response = make_api_call(URL.format(start))
        item_list = parse_market_history(market_api_response)
        full_item_list.extend(item_list)
        if is_log:
            print_page(page_num, item_list)

    return full_item_list


def load_item_list_from_json(path_to_data: str) -> List[Item]:
    with open(path_to_data, "r") as json_file:
        data: List[dict] = json.load(json_file)
        item_list = [Item(**item) for item in data]
        return item_list


def print_page(page_num: str | int, item_list: List[Item]) -> None:
    print("-" * 10 + f"СТРАНИЦА №{page_num}" + "-" * 10)
    for i, item in enumerate(item_list, start=1):
        print(f"{i}. {item.item_name}, {item.price}, {item.currency}")
    print("-" * 32)
