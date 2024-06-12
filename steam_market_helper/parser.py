from typing import List
from bs4 import BeautifulSoup
from .steam_market_helper_types import Item, MarketApiResponse, TransactionType


def parse_market_history(api_response: MarketApiResponse) -> List[Item]:
    text = api_response.html_page
    items = []
    soup = BeautifulSoup(text, "lxml")
    cell_items = soup.find_all(class_="market_listing_row market_recent_listing_row")
    for item in cell_items:
        cell_type = item.find(class_="market_listing_left_cell market_listing_gainorloss").text.strip()
        match cell_type:
            case "-":
                cell_data_type = TransactionType.sale.value
            case "+":
                cell_data_type = TransactionType.purchase.value
            case _:
                cell_data_type = TransactionType.listing.value
        item_name = item.find(class_="market_listing_item_name").text
        item_type = item.find(class_="market_listing_game_name").text
        date_combine = item.find_all(class_="market_listing_right_cell market_listing_listed_date can_combine")
        listed_on, acted_on = date_combine[1].text.strip(), date_combine[0].text.strip()
        price_row = item.find(class_="market_listing_price").text.strip()
        price_row = price_row[:-1].replace(",", ".").split(" ") if price_row else ["0", "operation_canceled"]
        price, currency = float(price_row[0]), price_row[1]

        items.append(Item(cell_data_type=cell_data_type,
                          item_name=item_name,
                          item_type=item_type,
                          listed_on=listed_on,
                          acted_on=acted_on,
                          price=price,
                          currency=currency))
    return items
