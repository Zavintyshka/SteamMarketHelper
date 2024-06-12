from steam_market_helper import funcs
from steam_market_helper import filter_funcs


def main():
    # print(funcs.dump_item_list_to_json("data/full_item_new.json"))
    item_list = funcs.get_item_list("./smh/new_data.json", from_file=True, is_test=False, delay=0, no_log=True)
    sorted_item_list = filter_funcs.get_sorted_item_list(item_list=item_list,
                                                         transaction="sale",
                                                         filter="price",
                                                         order="desc")
    funcs.beautiful_table(1, sorted_item_list)


if __name__ == "__main__":
    main()
