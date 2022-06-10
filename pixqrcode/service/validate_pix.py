import re

from pixqrcode.model.pix_error import PixError
from pixqrcode.model.pix import Pix
from pixqrcode.utils.format_values import FormatValues


class ValidatePix:
    is_valid = False

    def __init__(self, pix: Pix):
        self.pix = pix

    def validate(self):
        self.name()
        self.amount()
        self.city()
        self.reference_label()
        self.mobile()
        self.is_valid = True
        return self.is_valid

    def name(self):
        if not self.pix.name:
            raise PixError("Nome nao informado")

        self.pix.name = FormatValues.texts(self.pix.name)
        return True

    def city(self):
        if not self.pix.city:
            raise PixError("cidade nao informada")

        self.pix.city = FormatValues.texts(self.pix.city)
        return True

    def amount(self):
        if self.pix.amount:
            self.pix.amount = FormatValues.amount(self.pix.amount)
        else:
            self.pix.amount = "0.00"
        return True

    def reference_label(self):
        if not self.pix.reference_label:
            self.pix.reference_label = "***"
        else:
            self.pix.reference_label = FormatValues.texts_no_space(self.pix.reference_label)

    def validateCPF(self):
        cpf = self.pix.mobile
        cpf = re.sub('\D', '', cpf)

        numbers = [int(digit) for digit in cpf if digit.isdigit()]
        if len(numbers) != 11 or len(set(numbers)) == 1:
            return False

        sum_of_products = sum(a*b for a, b in zip(numbers[0:9], range(10, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[9] != expected_digit:
            return False

        sum_of_products = sum(a*b for a, b in zip(numbers[0:10], range(11, 1, -1)))
        expected_digit = (sum_of_products * 10 % 11) % 10
        if numbers[10] != expected_digit:
            return False

        return True

    """
        Valida o tipo de chave e retorna o codigo de acordo com o BC
    """
    def detect_type_key(self):
        key = self.pix.mobile
        regex = re.search(r'^[a-zA-Z0-9._-]+@[a-zA-Z0-9]+\.[a-zA-Z\.a-zA-Z]{1,10}$', key)
        # 0111 - CPF
        # 0111 - CNPJ
        # 0125 - EMAIL
        # 0114 - Telefone

        code = ""
        if regex is None:
            key_numbers = re.sub('\D', '', key)
            if len(key_numbers) == 10:
                #valida se é um telefone fixo
                code = '0114'

            if len(key_numbers) == 12:
                #valida se é um telefone com DDI
                code = '0114'

            if len(key_numbers) == 13:
                #valida se é um celular com DDI
                code = '0114'

            elif self.validateCPF():
                #valida se é um cpf com base nos calculos de digitos
                code = '0111'
            elif len(key_numbers) == 11:
                #se na ultima validacao nao retornou true é bem provavel que seja celular

                code = '0114'
            elif len(key_numbers) == 14:
                #verifica se é cnpj
                code = '0111' #creio que o codigo esteja errado, nao achei nada sobre
            else:
                raise Exception("A chave informada não foi identificada")
        else:
            # É email
            code = '0125'

        return code

    def mobile(self):
        if not self.pix.mobile:
            raise PixError("Chave nao informado")
        code = self.detect_type_key()
        if code == '0114':
            self.pix.mobile = FormatValues.mobile(self.pix.mobile)
            if not re.match(r'^.55[\d]{3}', self.pix.mobile):
                if not re.match(r'^55[\d]{3}', self.pix.mobile):
                    self.pix.mobile = f"+55{self.pix.mobile}"
                else:
                    self.pix.mobile = f"+{self.pix.mobile}"

            if 14 > len(self.pix.mobile) < 14:
                raise PixError("telefone curto ou longo")

            if not re.match(r'^.+55[\d]{3}', self.pix.mobile):
                raise PixError("telefone sem o DDD")
        return True
