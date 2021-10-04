import re


class FormatValues:
    @staticmethod
    def texts(text: str):
        return re.sub(r'[^0-9a-zA-Z\s]+', '', text)

    @staticmethod
    def amount(amount: str):
        value_base = re.sub(r'[^0-9]', '', amount).upper()
        return '{:.2f}'.format((int(value_base) / 100)).__str__()
        # return ('{:.2f}'.format(value_base / 100)).replace('.', ',')

    @staticmethod
    def mobile(mobile: str):
        return re.sub(r'[^0-9]', '', mobile).upper()

    @staticmethod
    def texts_no_space(text: str):
        return re.sub(r'[^0-9a-zA-Z]+', '', text)
