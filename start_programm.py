from steam_market_helper import funcs


def main():
    total_cost = sum(item.price for item in funcs.load_item_list_from_json("./full_item.json"))
    print(total_cost)


if __name__ == "__main__":
    main()
