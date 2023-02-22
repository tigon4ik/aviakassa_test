from __future__ import annotations

from enum import Enum, StrEnum

from pydantic import BaseModel, Field
from decimal import Decimal


class ObjectType(str, Enum):
    city = 'city'
    country = 'country'
    airport = 'airport'
    carrier = 'carrier'
    aircraft = 'aircraft'
    terminal = 'terminal'
    train_station = 'train_station'


class Loc(BaseModel):
    """Объект месторасположения """
    type: ObjectType = Field(..., description='Тип расположения')
    name: str = Field(..., description='Название расположения')


class ServiceType(StrEnum):
    avia = 'avia'
    hotel = 'hotel'
    rail = 'rail'


class BaseLocation(BaseModel):
    """Базовый класс расположения """
    country: Loc = Field(None, description='Страна')
    city: Loc = Field(None, description='Город')


class BaseSearchResult(BaseModel):
    """Базовый результат поиска """
    service_type: ServiceType = Field(..., description='Тип услуги')
    total: int = Field(..., description='Общее количество результатов поиска')
    page: int = Field(None, description='Номер страницы')
    limit: int = Field(None, description='Количество результатов поиска на странице')


class GeoPosition(BaseModel):
    latitude: Decimal
    longitude: Decimal


class HotelLocation(BaseLocation):
    """Расположение отеля """


class HotelFacility(BaseModel):
    name: str = Field(..., description='Название услуги')
    category: str = Field(..., description='Категория услуги')


class HotelBase(BaseModel):
    """Отель """
    id: str | None = Field(..., description='ID отеля')
    hotel_name: str = Field(..., description='Название')
    stars: int = Field(None, description='Количество звёзд')
    address: str = Field(..., description='Адрес')
    geo_position: GeoPosition = Field(None, description='Координаты отеля')
    location: HotelLocation = Field(..., description='Расположение отеля')
    is_recommended: bool = Field(None, description='Флаг рекомендуемого поставщиком отеля')
    facilities: list[HotelFacility] = Field([], description='Список услуг отеля')


class ShortHotelFacilities(BaseModel):
    wifi: bool | None = Field(None, description='Флаг о наличии услуги wifi')
    breakfast: bool | None = Field(None, description='Флаг о наличии завтрака')
    parking: bool | None = Field(None, description='Флаг о наличии парковки')
    registration_24: bool | None = Field(None, description='Наличие круглосуточной регистрации')
    gym: bool | None = Field(None, description='Флаг о наличии тренажерного зала')
    safe: bool | None = Field(None, description='Флаг о наличии сейфа')
    conditioning: bool | None = Field(None, description='Флаг о наличии кондиционера')
    luggage_storage: bool | None = Field(None, description='Флаг о наличии камеры хранения')


class Hotel(HotelBase):
    image_url: str = Field(None, description='Ссылка на изображение')
    description: str = Field(..., description='Описание')
    currency: str = Field(..., description='Валюта')
    min_price_per_night: Decimal | None = Field(
        ...,
        description='Минимальная стоимость за одну ночь',
    )
    short_facilities: ShortHotelFacilities | None = Field(None, description='Наличие важных услуг')


class HotelSearchResult(BaseSearchResult):
    """Результат поиска по отелям """
    service_type: ServiceType.hotel = Field(default=ServiceType.hotel, const=True)
    data: list[Hotel] = Field(..., description='Список отелей')
