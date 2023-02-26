import re

from hotel_converter.api import hotel_api
from hotel_converter.models import (
    HotelSearchResult,
    Hotel,
    HotelFacility,
    HotelLocation,
    Loc,
    ObjectType,
    ShortHotelFacilities
)


class HotelComparator:
    @staticmethod
    def compare(data: Hotel) -> tuple:
        return (
            data.is_recommended,
            data.image_url is None,
            data.min_price_per_night,
            data.stars,
            bool(data.facilities)
        )


class HotelConverter:
    def convert(self, data: dict) -> HotelSearchResult:
        hotels = map(self.convertHotel, data.get('hotels'))
        hotels = sorted(hotels, key=HotelComparator.compare, reverse=True)
        return HotelSearchResult(
            total=data.get('total'),
            page=data.get('offset'),
            limit=data.get('limit'),
            data=hotels
        )

    def convertHotel(self, hotel: dict) -> Hotel:
        hotel = Hotel(
            id=hotel.get('id'),
            hotel_name=hotel.get('name'),
            stars=hotel.get('stars'),
            address=hotel.get('address'),
            geo_position=hotel.get('location'),
            location=self.convertLocation(hotel),
            is_recommended=hotel.get('is_provider_contract'),
            facilities=self.convertFacilities(hotel.get("facilities")),
            image_url=next(iter(map(lambda photo: photo.get('url'), hotel.get('photos'))), None),
            currency=next(iter(hotel.get("price_details")), None),
            description=hotel.get('description'),
            min_price_per_night=hotel.get('min_price')
        )
        hotel.short_facilities = self.convertShortFacilities(hotel.facilities)
        return hotel

    def convertShortFacilities(
            self,
            facilities: list[HotelFacility]
    ) -> ShortHotelFacilities:
        facilityNames = map(lambda facility: facility.name, facilities)
        facilityNames = list(map(lambda name: name.lower(), facilityNames))
        return ShortHotelFacilities(
            wifi=any(map(HotelConverter.checkWiFi, facilityNames)),
            breakfast=any(map(HotelConverter.checkBreakfast, facilityNames)),
            parking=any(map(HotelConverter.checkParking, facilityNames)),
            registration_24=any(map(HotelConverter.checkRegistration, facilityNames)),
            gym=any(map(HotelConverter.checkGym, facilityNames)),
            safe=any(map(HotelConverter.checkSafe, facilityNames)),
            conditioning=any(map(HotelConverter.checkConditioning, facilityNames)),
            luggage_storage=any(map(HotelConverter.checkLuggageStorage, facilityNames))
        )

    def convertLocation(self, hotel) -> HotelLocation:
        return HotelLocation(
            city=HotelConverter.generateLoc(hotel, 'city'),
            country=HotelConverter.generateLoc(hotel, 'country')
        )

    def convertFacilities(self, facilities: list) -> list[HotelFacility]:
        convertedSubFacilities = map(self.convertSubFacilities, facilities)
        return [facility for subFacilities in convertedSubFacilities for facility in subFacilities]

    def convertSubFacilities(self, facilities: dict) -> list[HotelFacility]:
        return list(map(
            lambda facility: HotelFacility(name=facility, category=facilities.get('name')),
            facilities.get('list')))

    @staticmethod
    def generateLoc(data: dict, objectType: str) -> Loc:
        return Loc(
            type=ObjectType[objectType],
            name=data.get(objectType)
        )

    @staticmethod
    def checkWiFi(data: str) -> bool:
        return bool(re.search(r"\bwi-?fi\b", data))

    @staticmethod
    def checkBreakfast(data: str) -> bool:
        return bool(re.search(r"\bзавтрак\b", data))

    @staticmethod
    def checkParking(data: str) -> bool:
        return bool(re.search(r"\bпарковка\b", data))

    @staticmethod
    def checkRegistration(data: str) -> bool:
        return bool(re.search(r"\bкруглосуточная\b", data))

    @staticmethod
    def checkGym(data: str) -> bool:
        return bool(re.search(r"\bтренажерный\b", data))

    @staticmethod
    def checkSafe(data: str) -> bool:
        return bool(re.search(r"\bсейф\b", data))

    @staticmethod
    def checkConditioning(data: str) -> bool:
        return bool(re.search(r"\bкондиционер\b", data))

    @staticmethod
    def checkLuggageStorage(data: str) -> bool:
        return bool(re.search(r"\bхранени[ея]\b\s\bбагажа\b", data))


def main():
    converter = HotelConverter()
    result = hotel_api.get_hotels()
    return converter.convert(result)


if __name__ == '__main__':
    main()
