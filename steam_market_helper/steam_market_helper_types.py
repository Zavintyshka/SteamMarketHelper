from collections import namedtuple
from enum import Enum

Item = namedtuple("Item", ["cell_data_type", "item_name", "item_type", "listed_on", "acted_on", "price", "currency"])
MarketApiResponse = namedtuple("MarketApiResponse", ["html_page", "total_items"])


class CellDataType(Enum):
    sale = "sale"
    purchase = "purchase"
    listing = "listing"
