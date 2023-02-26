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


class TestShortFacilities(unittest.TestCase):
    defaultShortFacilities = None

    def setUp(self) -> None:
        self.defaultShortFacilities = TestShortFacilities.createShortFacilities()

    # Кейс с минимальным заполнением данных
    def testFacilitiesCase0(self):
        hotel_api.get_hotels = Mock(return_value=TEST_HOTEL_RESULTS_RESPONSE_CASE_0)
        result = main().data[0].short_facilities
        self.assertEqual(result, self.defaultShortFacilities)

    # Кейс с одним заполнением
    def testFacilitiesCase1(self):
        self.defaultShortFacilities.wifi = True
        hotel_api.get_hotels = Mock(return_value=TEST_HOTEL_RESULTS_RESPONSE_CASE_1)
        result = main().data[0].short_facilities
        self.assertEqual(result, self.defaultShortFacilities)

    # Кейс с нескольким заполнением
    def testFacilitiesCase2(self):
        self.defaultShortFacilities.wifi = True
        self.defaultShortFacilities.parking = True
        self.defaultShortFacilities.registration_24 = True
        self.defaultShortFacilities.luggage_storage = True
        self.defaultShortFacilities.conditioning = True
        self.defaultShortFacilities.safe = True
        hotel_api.get_hotels = Mock(return_value=TEST_HOTEL_RESULTS_RESPONSE_CASE_4)
        result = main().data[0].short_facilities
        self.assertEqual(result, self.defaultShortFacilities)

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
