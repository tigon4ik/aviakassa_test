from hotel_converter.api import hotel_api
from hotel_converter.models import HotelSearchResult


class HotelConverter:
    def convert(self, data: dict) -> HotelSearchResult:
        pass


def main():
    converter = HotelConverter()
    result = hotel_api.get_hotels()
    return converter.convert(result)


if __name__ == '__main__':
    main()
