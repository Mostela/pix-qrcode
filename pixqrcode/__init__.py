import base64
import os.path
from io import BytesIO

import qrcode

from pixqrcode.model import Pix, PixError
from pixqrcode.service import GenerateCode, ValidatePix


class PixQrCode:
    def __init__(self, name: str, mobile: str, city: str, amount: str = None, reference_label: str = None):
        """
    Definiçao da classe para implementaçao e geraçao do QRCode
        :param name: Nome do destinatario
        :param mobile: Telefone celular do destinatario
        :param city: Cidade do remetente
        :param amount: Valor da transaçao
        :param reference_label: Codigo da transaçao
        """
        self.pix = Pix(name, mobile, city, amount, reference_label)

    def is_valid(self) -> bool:
        """
    Valida os campos informados
        :return: bool
        """
        validate = ValidatePix(self.pix)
        # FIXME: Better return errors
        return validate.validate()

    def generate_code(self):
        """
    Codigo para geracao da QRCode
        :return: str
        """
        generator_code = GenerateCode()
        if self.is_valid():
            return generator_code.format_code(self.pix).strip()

    def save_qrcode(self, folder: str, filename: str, **kwargs):
        """
    Salva o QRCode em um local especifico
        :param folder: Pasta onde salvar o arquivo
        :param filename: Nome do arquivo
        :param kwargs:
        """
        if os.path.isdir(folder):
            brcode = qrcode.make(self.generate_code())
            brcode.save(f"{folder}/{filename}.png", 'PNG', **kwargs)
        else:
            raise PixError("não é uma pasta onde salvar")

    def export_base64(self, **kwargs):
        """
    Exporta o QRCode gerado em forma de Base64 type image PNG
        :param kwargs:
        :return: str
        """
        try:
            bytes_io = BytesIO()
            brcode = qrcode.make(self.generate_code())
            brcode.save(bytes_io, 'PNG', **kwargs)
            base64_header = "data:image/png;base64,"
            return f"{base64_header}{base64.b64encode(bytes_io.getvalue()).decode()}"
        except Exception as ex:
            print(ex)
