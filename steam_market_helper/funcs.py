import json
from time import sleep
from typing import List
from prettytable import PrettyTable
from .steam_market_helper_types import Item
from .api_call import make_api_call
from .parser import parse_market_history
from .settings import URL

__all__ = ["dump_item_list_to_json", "get_item_list"]


def dump_item_list_to_json(path: str, delay: int, no_log: bool, is_test: bool):
    item_list = get_item_list(from_file=False, delay=delay, no_log=no_log, is_test=is_test, path=path)
    with open(path, "w") as json_file:
        json.dump([*(item._asdict() for item in item_list)], json_file)


def get_item_list(path: str,
                  from_file: bool,
                  delay: int,
                  no_log: bool,
                  is_test: bool,
                  transaction_type: str,
                  filter: str,
                  order: str) -> List[Item]:
    if from_file:
        return load_item_list_from_json(path=path, no_log=no_log)
    return load_item_list_from_api(is_test=is_test, delay=delay, no_log=no_log)


def load_item_list_from_api(is_test: bool = True, delay: int = 0, no_log: bool = False) -> List[Item]:
    full_item_list = []
    market_api_response = make_api_call(URL.format("0"))
    first_item_list = parse_market_history(market_api_response)
    full_item_list.extend(first_item_list)
    if is_test:
        if not no_log:
            beautiful_table(page_num=1, item_list=first_item_list)
        return first_item_list

    total_items = market_api_response.total_items
    paginator = (start * 10 for start in range(1, (total_items // 10) + 1))
    if not no_log:
        beautiful_table("1", item_list=first_item_list)

    for page_num, start in enumerate(paginator, start=2):
        market_api_response = make_api_call(URL.format(start))
        item_list = parse_market_history(market_api_response)
        full_item_list.extend(item_list)
        if not no_log:
            beautiful_table(page_num, item_list)
        sleep(delay)

    return full_item_list


def load_item_list_from_json(path: str, no_log: bool) -> List[Item]:
    with open(path, "r") as json_file:
        data: List[dict] = json.load(json_file)
        item_list = [Item(**item) for item in data]
        if not no_log:
            beautiful_table(1, item_list)
        return item_list


def beautiful_table(page_num, item_list):
    p_table = PrettyTable()
    p_table.title = f"Страница No.{page_num}"
    p_table.field_names = ["No", "cell_data_type", "item_name", "item_type", "listed_on", "acted_on", "price",
                           "currency"]

    for i, item in enumerate(item_list, start=1):
        p_table.add_row([i, *item._asdict().values()])
    print(p_table)
