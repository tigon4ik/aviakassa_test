Описание:

Мы получаем от провайдера данные о поиске с помощью метода hotel_api.get_hotels,
полученные данные необходимо конвертировать во внутренний формат в классе _HotelConverter_.

Все необходимые модели находятся в файле models.py
short_facilities - это флаги наличия определенных видов услуг

**is_recommended == is_provider_contract**

Выход отелей должен быть отсортирован по умолчанию: 
Поля сортировки и их порядок

    - is_recommended
    - есть фото
    - минимальная цена за ночь
    - количество звезд
    - переданы ли услуги

Задачи:

    - Написать реализацию класса _HotelConverter_
    - Написать тесты на main, обязательно сделать мок на hotel_api.get_hotels, так же отдельным тестом short_facilities с несколькими вариантами
    - Использовать flake8 

