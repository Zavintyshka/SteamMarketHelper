from steam_market_helper import make_api_call, parse_market_history


def main():
    market_api_response = make_api_call()
    print(f"Total items: {market_api_response.total_items}")
    items = parse_market_history(market_api_response)
    print(len(items), items)


if __name__ == "__main__":
    main()
