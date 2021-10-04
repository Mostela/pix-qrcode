# Pix QRCode - Python

#### Version: __1.0__


Para geraçao de codigos QR e facilitar pagamentos ao consumidor

## Exemplo

Crie a funçao PixQrCode abaixo e defina os parametros em ordem

* nome
* telefone (Chave PIX)
* Cidade de envio
* Valor de envio


    pix = PixQrCode("Fulano De Tal", "(70) 97070-7070", "Brasilia", "100")


### Retorno do QRCode

O QRCode utiliza a biblioteca Pillow como base e aceita os seus parametros para serem gerados, como opacidade, cor e tamanho se necessario

    pix.export_base64()

Exporta o QR Code como formato de base64 type image. Para exibiçao direta em tag HTML

    pix.save_qrcode(folder, filename, **kwargs)

Salva o QRCode em uma pasta com um nome de arquivo. Formato padrao e PNG (Portable Network Graphic)
    
    pix.generate_code()

Gera a hash convertida em QRCode e interpletada pelos bancos na imagem
