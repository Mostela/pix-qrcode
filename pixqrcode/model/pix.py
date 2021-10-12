

class Pix:
    country_code = "BR"
    merchant_category_code = "0000"
    transaction_currency = "986"
    name = None
    city = None
    mobile = None
    amount = "0"
    reference_label = None

    def __init__(self, name, mobile, city, amount=0, reference_label="***") -> None:
        super().__init__()
        self.name = name
        self.city = city
        self.amount = amount
        self.mobile = mobile
        self.reference_label = reference_label
