import unittest
from unittest.mock import Mock

from hotel_converter.models import (
    HotelSearchResult,
    Hotel,
    HotelLocation,
    Loc,
    ObjectType,
    ShortHotelFacilities,
    HotelFacility
)
from hotel_converter.api import hotel_api
from dataCases import *
from main import main


class TestHotelConverter(unittest.TestCase):
    defaultHotelSearchResult = None

    def setUp(self) -> None:
        self.defaultHotelSearchResult = TestHotelConverter.createHotelSearchResult()

    # Кейс с минимальным заполнением данных
    def testConvertCase0(self):
        hotel_api.get_hotels = Mock(return_value=TEST_HOTEL_RESULTS_RESPONSE_CASE_0)
        result = main()
        self.assertEqual(result, self.defaultHotelSearchResult)

    # Кейс с некоторым заполнением данных
    def testConvertCase1(self):
        hotel = self.defaultHotelSearchResult.data[0]
        hotel.stars = 2
        hotel.is_recommended = False
        hotel.image_url = "some_url"
        hotel.facilities = [HotelFacility(name="Wi-Fi", category="Сервисы")]
        hotel.short_facilities.wifi = True

        hotel_api.get_hotels = Mock(return_value=TEST_HOTEL_RESULTS_RESPONSE_CASE_1)
        result = main()
        self.assertEqual(result, self.defaultHotelSearchResult)

    # проверка последовательности
    def testConvertCase2(self):
        self.defaultHotelSearchResult.total = 2
        hotel1 = self.defaultHotelSearchResult.data[0]
        hotel2 = TestHotelConverter.createHotel()
        hotel1.id = '1'
        hotel1.stars = 2
        hotel1.is_recommended = True
        hotel2.stars = 5
        hotel2.is_recommended = False
        self.defaultHotelSearchResult.data.append(hotel2)

        hotel_api.get_hotels = Mock(return_value=TEST_HOTEL_RESULTS_RESPONSE_CASE_2)
        result = main()
        self.assertEqual(result, self.defaultHotelSearchResult)

    # Кейс без отелей
    def testConvertCase4(self):
        self.defaultHotelSearchResult.data = []
        hotel_api.get_hotels = Mock(return_value=TEST_HOTEL_RESULTS_RESPONSE_CASE_3)
        result = main()
        self.assertEqual(result, self.defaultHotelSearchResult)

    @staticmethod
    def createHotelSearchResult() -> HotelSearchResult:
        return HotelSearchResult(
            total=1,
            page=0,
            limit=20,
            data=[TestHotelConverter.createHotel()]
        )

    @staticmethod
    def createHotel() -> Hotel:
        return Hotel(
            id=0,
            description="someDescription",
            currency="RUB",
            min_price_per_night=400,
            hotel_name="myHotel",
            address="myAddress",
            location=HotelLocation(
                city=Loc(type=ObjectType.city, name="Москва"),
                country=Loc(type=ObjectType.country, name="Россия")
            ),
            short_facilities=TestHotelConverter.createShortFacilities()
        )

    @staticmethod
    def createShortFacilities() -> ShortHotelFacilities:
        return ShortHotelFacilities(
            wifi=False,
            breakfast=False,
            parking=False,
            registration_24=False,
            gym=False,
            safe=False,
            conditioning=False,
            luggage_storage=False,
        )


if __name__ == '__main__':
    unittest.main()
