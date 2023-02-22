from hotel_converter.data import TEST_HOTEL_RESULTS_RESPONSE


class HotelApi:
    def get_hotels(self):
        """
        Тут условно делаем запрос в апи и получаем результат
        :return:
        """
        return TEST_HOTEL_RESULTS_RESPONSE


hotel_api = HotelApi()
