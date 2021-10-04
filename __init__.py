import base64
import os.path
from io import BytesIO

import qrcode

from model.pix import Pix
from model.pix_error import PixError
from service.generate_code import GenerateCode
from service.validate_pix import ValidatePix


class PixQrCode:
    def __init__(self, name: str, mobile: str, city: str, amount: str = None, reference_label: str = None):
        self.pix = Pix(name, mobile, city, amount, reference_label)

    def is_valid(self):
        validate = ValidatePix(self.pix)
        # FIXME: Better return errors
        return validate.validate()

    def generate_code(self):
        generator_code = GenerateCode()
        if self.is_valid():
            return generator_code.format_code(self.pix).strip()

    def save_qrcode(self, folder: str, filename: str, **kwargs):
        if os.path.isdir(folder):
            brcode = qrcode.make(self.generate_code())
            brcode.save(f"{folder}/{filename}.png", 'PNG', **kwargs)
        else:
            raise PixError("não é uma pasta onde salvar")

    def export_base64(self, **kwargs):
        try:
            bytes_io = BytesIO()
            brcode = qrcode.make(self.generate_code())
            brcode.save(bytes_io, 'PNG', **kwargs)
            base64_header = "data:image/png;base64,"
            return f"{base64_header}{base64.b64encode(bytes_io.getvalue()).decode()}"
        except Exception as ex:
            print(ex)
