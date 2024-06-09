from collections import namedtuple

Item = namedtuple("Item", ["item_name", "price", "currency"])
MarketApiResponse = namedtuple("MarketApiResponse", ["html_page", "total_items"])
