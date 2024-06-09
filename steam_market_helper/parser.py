from typing import List
from bs4 import BeautifulSoup
from .steam_market_helper_types import Item, MarketApiResponse


def parse_market_history(api_response: MarketApiResponse) -> List[Item]:
    text = api_response.html_page
    items = []
    soup = BeautifulSoup(text, "lxml")
    sell_items = soup.find_all(class_="market_listing_row market_recent_listing_row")
    for item in sell_items:
        item_name = item.find(class_="market_listing_item_name").text
        price_row = item.find(class_="market_listing_price").text.strip()
        price_row = price_row[:-1].replace(",", ".").split(" ") if price_row else ["0", "operation_canceled"]
        price, currency = float(price_row[0]), price_row[1]
        items.append(Item(item_name=item_name, price=price, currency=currency))
    return items
