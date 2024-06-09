from requests import get
from .steam_market_helper_types import MarketApiResponse
from .settings import URL, HEADERS


def make_api_call() -> MarketApiResponse:
    response = get(URL, headers=HEADERS).json()
    return MarketApiResponse(html_page=response["results_html"], total_items=response["total_count"])
