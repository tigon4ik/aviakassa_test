TEST_HOTEL_RESULTS_RESPONSE_CASE_0 = {
    'search_id': 'some_id',
    'search': {
        'adults': 1,
        'children': [],
        'rooms': [{'guests': [{'age': 30, 'is_child': False, 'citizenship': 'ru'}]}],
        'check_in': '26.06.2022',
        'check_out': '01.07.2022',
        'city': 6308866,
        'hotel_id': None,
        'location': {
            'iata': 6308866,
            'country': 'Россия',
            'type': 'City',
            'type_description': 'Город',
            'typeRu': 'Город',
            'name': 'Белогорск, Россия',
        },
    },
    'hotels': [
        {
            'id': '0',
            'name': 'myHotel',
            'phone': None,
            'email': None,
            'photos': [],
            'description': 'someDescription',
            'policy': None,
            'facilities': [],
            'category_name': 'Hotel',
            'rating': [],
            'address': 'myAddress',
            'city': 'Москва',
            'country': 'Россия',
            'trip_advisor_rating': None,
            'check_in_time': '14:00',
            'check_out_time': '12:00',
            'max_check_in_time': None,
            'max_check_out_time': None,
            'important_information': None,
            'min_fare': 487,
            'min_fares': {'RUB': 487},
            'min_price': 400,
            'min_prices': {'RUB': 400},
            'price_details': {'RUB': {'aac_fee': 0}},
            'liked': False,
            'has_free_cancellation': True,
            'travel_policy': {'is_violated': False, 'notices': [], 'reason_codes': []},
            'search_id': 'some_hotel_id',
            'contract': None,
            'is_contract_only': False,
        }
    ],
    'total': 1,
    'offset': 0,
    'limit': 20,
    'is_completed': True,
}

TEST_HOTEL_RESULTS_RESPONSE_CASE_1 = {
    'search_id': 'some_id',
    'search': {
        'adults': 1,
        'children': [],
        'rooms': [{'guests': [{'age': 30, 'is_child': False, 'citizenship': 'ru'}]}],
        'check_in': '26.06.2022',
        'check_out': '01.07.2022',
        'city': 6308866,
        'hotel_id': None,
        'location': {
            'iata': 6308866,
            'country': 'Россия',
            'type': 'City',
            'type_description': 'Город',
            'typeRu': 'Город',
            'name': 'Белогорск, Россия',
        },
    },
    'hotels': [
        {
            'id': '0',
            'name': 'myHotel',
            'phone': None,
            'email': None,
            'description': 'someDescription',
            'policy': None,
            'photos': [
                {
                    'url': 'some_url',
                    'thumb': 'some_thumb',
                },
            ],
            'facilities': [
                {'name': 'Сервисы', 'list': ['Wi-Fi']},
            ],
            'category_name': 'Hotel',
            'rating': [],
            'address': 'myAddress',
            'city': 'Москва',
            'country': 'Россия',
            'trip_advisor_rating': None,
            'check_in_time': '14:00',
            'check_out_time': '12:00',
            'max_check_in_time': None,
            'max_check_out_time': None,
            'important_information': None,
            'min_fare': 487,
            'min_fares': {'RUB': 487},
            'min_price': 400,
            'min_prices': {'RUB': 400},
            'price_details': {'RUB': {'aac_fee': 0}},
            'liked': False,
            'has_free_cancellation': True,
            'travel_policy': {'is_violated': False, 'notices': [], 'reason_codes': []},
            'search_id': 'some_hotel_id',
            'contract': None,
            'is_contract_only': False,
            'stars': 2,
            'is_provider_contract': False,
        }
    ],
    'total': 1,
    'offset': 0,
    'limit': 20,
    'is_completed': True,
}

TEST_HOTEL_RESULTS_RESPONSE_CASE_2 = {
    'search_id': 'some_id',
    'search': {
        'adults': 1,
        'children': [],
        'rooms': [{'guests': [{'age': 30, 'is_child': False, 'citizenship': 'ru'}]}],
        'check_in': '26.06.2022',
        'check_out': '01.07.2022',
        'city': 6308866,
        'hotel_id': None,
        'location': {
            'iata': 6308866,
            'country': 'Россия',
            'type': 'City',
            'type_description': 'Город',
            'typeRu': 'Город',
            'name': 'Белогорск, Россия',
        },
    },
    'hotels': [
        {
            'id': '0',
            'name': 'myHotel',
            'phone': None,
            'email': None,
            'description': 'someDescription',
            'policy': None,
            'photos': [],
            'facilities': [],
            'category_name': 'Hotel',
            'rating': [],
            'address': 'myAddress',
            'city': 'Москва',
            'country': 'Россия',
            'trip_advisor_rating': None,
            'check_in_time': '14:00',
            'check_out_time': '12:00',
            'max_check_in_time': None,
            'max_check_out_time': None,
            'important_information': None,
            'min_fare': 487,
            'min_fares': {'RUB': 487},
            'min_price': 400,
            'min_prices': {'RUB': 400},
            'price_details': {'RUB': {'aac_fee': 0}},
            'liked': False,
            'has_free_cancellation': True,
            'travel_policy': {'is_violated': False, 'notices': [], 'reason_codes': []},
            'search_id': 'some_hotel_id',
            'contract': None,
            'is_contract_only': False,
            'stars': 5,
            'is_provider_contract': False,
        },
{
            'id': '1',
            'name': 'myHotel',
            'phone': None,
            'email': None,
            'description': 'someDescription',
            'policy': None,
            'photos': [],
            'facilities': [],
            'category_name': 'Hotel',
            'rating': [],
            'address': 'myAddress',
            'city': 'Москва',
            'country': 'Россия',
            'trip_advisor_rating': None,
            'check_in_time': '14:00',
            'check_out_time': '12:00',
            'max_check_in_time': None,
            'max_check_out_time': None,
            'important_information': None,
            'min_fare': 487,
            'min_fares': {'RUB': 487},
            'min_price': 400,
            'min_prices': {'RUB': 400},
            'price_details': {'RUB': {'aac_fee': 0}},
            'liked': False,
            'has_free_cancellation': True,
            'travel_policy': {'is_violated': False, 'notices': [], 'reason_codes': []},
            'search_id': 'some_hotel_id',
            'contract': None,
            'is_contract_only': False,
            'stars': 2,
            'is_provider_contract': True,
        }
    ],
    'total': 2,
    'offset': 0,
    'limit': 20,
    'is_completed': True,
}

TEST_HOTEL_RESULTS_RESPONSE_CASE_3 = {
    'search_id': 'some_id',
    'search': {
        'adults': 1,
        'children': [],
        'rooms': [{'guests': [{'age': 30, 'is_child': False, 'citizenship': 'ru'}]}],
        'check_in': '26.06.2022',
        'check_out': '01.07.2022',
        'city': 6308866,
        'hotel_id': None,
        'location': {
            'iata': 6308866,
            'country': 'Россия',
            'type': 'City',
            'type_description': 'Город',
            'typeRu': 'Город',
            'name': 'Белогорск, Россия',
        },
    },
    'hotels': [],
    'total': 1,
    'offset': 0,
    'limit': 20,
    'is_completed': True,
}

TEST_HOTEL_RESULTS_RESPONSE_CASE_4 = {
    'search_id': 'some_id',
    'search': {
        'adults': 1,
        'children': [],
        'rooms': [{'guests': [{'age': 30, 'is_child': False, 'citizenship': 'ru'}]}],
        'check_in': '26.06.2022',
        'check_out': '01.07.2022',
        'city': 6308866,
        'hotel_id': None,
        'location': {
            'iata': 6308866,
            'country': 'Россия',
            'type': 'City',
            'type_description': 'Город',
            'typeRu': 'Город',
            'name': 'Белогорск, Россия',
        },
    },
    'hotels': [
        {
            'id': '0',
            'name': 'myHotel',
            'phone': None,
            'email': None,
            'photos': [],
            'description': 'someDescription',
            'policy': None,
            'facilities': [
                {
                    'name': 'Общие',
                    'list': [
                        'Wi-Fi доступен на всей территории',
                        'Платный Wi-Fi',
                        'Парковка',
                        'Бесплатная парковка',
                        'Парковка на территории',
                        'Смешанная парковка',
                        'Допускается размещение домашних животных',
                    ],
                },
                {'name': 'Сервисы', 'list': ['Wi-Fi']},
                {
                    'name': 'Стойка регистрации',
                    'list': ['Сейф', 'Камера хранения багажа', 'Круглосуточная стойка регистрации']
                },
                {'name': 'Разное', 'list': ['Кондиционер']},
                {
                    'name': 'Услуги бизнес-центра',
                    'list': [
                        'Конференц-зал/Банкетный зал',
                        'Факс/Ксерокопирование',
                        'Комната переговоров',
                    ],
                },
                {
                    'name': 'Питание и напитки',
                    'list': ['Бар', 'Ресторан (меню)', 'Электрический чайник'],
                },
            ],
            'category_name': 'Hotel',
            'rating': [],
            'address': 'myAddress',
            'city': 'Москва',
            'country': 'Россия',
            'trip_advisor_rating': None,
            'check_in_time': '14:00',
            'check_out_time': '12:00',
            'max_check_in_time': None,
            'max_check_out_time': None,
            'important_information': None,
            'min_fare': 487,
            'min_fares': {'RUB': 487},
            'min_price': 400,
            'min_prices': {'RUB': 400},
            'price_details': {'RUB': {'aac_fee': 0}},
            'liked': False,
            'has_free_cancellation': True,
            'travel_policy': {'is_violated': False, 'notices': [], 'reason_codes': []},
            'search_id': 'some_hotel_id',
            'contract': None,
            'is_contract_only': False,
        }
    ],
    'total': 1,
    'offset': 0,
    'limit': 20,
    'is_completed': True,
}
