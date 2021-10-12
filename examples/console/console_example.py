from pixqrcode import PixQrCode

name = input("Informe o nome\n")
mobile = input("Informe o celular\n")
city = input("Informe a cidade atual\n")
amount = input("Informe o valor\n")

pix = PixQrCode(name, mobile, city, amount)
pix.save_qrcode(".", f"pix-{name}")
