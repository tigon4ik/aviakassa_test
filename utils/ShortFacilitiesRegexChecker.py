import re


class ShortFacilitiesRegexChecker:
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