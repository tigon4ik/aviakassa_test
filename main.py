import re

from hotel_converter.api import hotel_api
from hotel_converter.models import HotelSearchResult, Hotel, HotelFacility, HotelLocation, Loc, ObjectType, \
    ShortHotelFacilities


# Вопросы
# 1) Фото представлены как список, а класс принимает только одну строку. Какой из урлов присваивать? Первый?
# 2)
#
class HotelConverter:
    def convert(self, data: dict) -> HotelSearchResult:
        # result = map(HotelConverter.reformHotelName, data.pop('hotels'))
        # result = map(HotelConverter.reformHotelCurrency, result)
        # result = map(HotelConverter.reformHotelMinPrice, result)
        # result = map(HotelConverter.reformFacilities, result)
        # data["data"] = list(result)
        # return HotelSearchResult.parse_obj(data)

        return HotelSearchResult(
            total=data.get('total'),
            page=data.get('offset'),
            limit=data.get('limit'),
            data=list(map(self.convertHotel, data.get('hotels')))
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

    def convertShortFacilities(self, facilities: list[HotelFacility]) -> ShortHotelFacilities:
        return ShortHotelFacilities(
            wifi=any(map(lambda facility: HotelConverter.checkWiFi(facility.name.lower()), facilities)),
            breakfast=any(map(lambda facility: HotelConverter.checkBreakfast(facility.name.lower()), facilities)),
            parking=any(map(lambda facility: HotelConverter.checkParking(facility.name.lower()), facilities)),
            registration_24=any(map(lambda facility: HotelConverter.checkRegistration(facility.name.lower()), facilities)),
            gym=any(map(lambda facility: HotelConverter.checkGym(facility.name.lower()), facilities)),
            safe=any(map(lambda facility: HotelConverter.checkSafe(facility.name.lower()), facilities)),
            conditioning=any(map(lambda facility: HotelConverter.checkConditioning(facility.name.lower()), facilities)),
            luggage_storage=any(map(lambda facility: HotelConverter.checkLuggageStorage(facility.name.lower()), facilities))
        )
        # return shortHotelFacilities

    def convertLocation(self, hotel) -> HotelLocation:
        return HotelLocation(
            city=HotelConverter.generateLoc(hotel, 'city'),
            country=HotelConverter.generateLoc(hotel, 'country')
        )

    def convertFacilities(self, facilities: list) -> list[HotelFacility]:
        convertedSubFacilities = map(self.convertSubFacilities, facilities)
        return [facility for subFacilities in convertedSubFacilities for facility in subFacilities]

    def convertSubFacilities(self, facilities: dict) -> list[HotelFacility]:
        return list(map(lambda facility: HotelFacility(
            name=facility,
            category=facilities.get('name')
        ), facilities.get('list')))

    @staticmethod
    def generateLoc(data: dict, objectType: str) -> Loc:
        return Loc(
            type=ObjectType[objectType],
            name=data.get(objectType)
        )

    @staticmethod
    def checkWiFi(data: str) -> bool:
        return bool(re.match(r"\bwi-?fi\b", data))

    @staticmethod
    def checkBreakfast(data: str) -> bool:
        return bool(re.match(r"\bзавтрак\b", data))

    @staticmethod
    def checkParking(data: str) -> bool:
        return bool(re.match(r"\bпарковка\b", data))

    @staticmethod
    def checkRegistration(data: str) -> bool:
        return bool(re.match(r"\bкруглосуточная\b", data))

    @staticmethod
    def checkGym(data: str) -> bool:
        return bool(re.match(r"\bтренажерный\b", data))

    @staticmethod
    def checkSafe(data: str) -> bool:
        return bool(re.match(r"\bсейф\b", data))

    @staticmethod
    def checkConditioning(data: str) -> bool:
        return bool(re.match(r"\bкондиционер\b", data))

    @staticmethod
    def checkLuggageStorage(data: str) -> bool:
        return bool(re.match(r"хранени[ея]\sбагажа", data))


def main():
    converter = HotelConverter()
    result = hotel_api.get_hotels()
    return converter.convert(result)


if __name__ == '__main__':
    main()
