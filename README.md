# Pix QRCode - Python

#### Versao: __1.0__

Biblioteca para a geração de codigos QR (BRCode como chamados na documentação do BACEN) a fins de facilitar a exibição para pagamentos ao consumidor.

## O que é pix

_Pix é o meio de pagamento eletrônico instantâneo, gratuito e com segurança, do Brasil. A iniciação de um Pix para uma pessoa física é gratuita._ [Wikipedia](https://pt.wikipedia.org/wiki/Pix)


## Isenção de responsabilidade

Os QR codes não foram testados aos bancos, sempre antes de transferir verifique se as informações estão corretas. O autor e contribuidores se isenta de qualquer responsabilidade pela exatidão e integridade das informações divulgada.


## Documentação de implementação BACEN - Banco Central do Brasil

[Manual BRCode](https://www.bcb.gov.br/content/estabilidadefinanceira/spb_docs/ManualBRCode.pdf)

[Especificações técnicas e de negócio do ecossistema de pagamentos instantâneos brasileiro](https://www.bcb.gov.br/content/estabilidadefinanceira/forumpireunioes/Documento%20de%20especifica%C3%A7%C3%B5es%20-%20vers%C3%A3o%205-0.pdf)

[Github Bacen](https://github.com/bacen)

**NÃO EXISTE NENHUMA INTEGRAÇÃO COM BANCOS**

---

## Exemplo basico

Importe a biblioteca do pip `pip install pixqrcode`

Importe a classe `from pixqrcode import PixQrCode` e defina os parametros como abaixo

Obrigatorio

* name = Nome do destinatario
* mobile (Chave PIX) = Telefone do destinatario _Em Breve mais chaves_
* city = Cidade de remetente


Opcional

* amount = Valor a ser enviado
    
    Valores serão sempre contados com 3 casas decimais e tem todos os digitos não numericos removidos, exemplos abaixo
    
    * R$ 1,00 = 100
    * R$ 10,00 = 1000
    
* reference_label = Código da transferência. Codigo não obrigatorio mais pode auxiliar em casos como ecommerce e vendas diretas por Pix



    `pix = PixQrCode("Fulano De Tal", "(70) 97070-7070", "Brasilia", "100")`


### Retorno do QRCode e codigo BRCode

seguimos com o objeto de cima definido iremos chamar os metodos e suas funções


#### Metodos


### `is_valid()`

Verifica se todos os campos inseridos são validos e pode seguir com a geração do QRCode. Retorna um valor boolean


### `export_base64()`

Retorna direto em formato base64 tipo imagem PNG (Portable Network Grapich) para ser renderizado dentro de uma tag img HTML ou ser transportado por uma API e demais usos.


    pix.export_base64()
    
    <img src='{pix_image}' alt='qrcode pagamento'/>



### `save_qrcode(folder, filename, **kwargs)`

    pix.save_qrcode("/pixs","pix-fulano")

Caso queira você pode salvar o codigo gerado em uma pasta com um nome especifico para ter o codigo. **Não precisa especificar o formato do arquivo sempre será PNG**

Pode retornar o valor dentro BufferIO para ser novamente processado.

A geração do QRCode é feita com a biblioteca [Pillow](https://pillow.readthedocs.io/en/stable/) então você pode utilizar para deixar seu QRCode ainda mais personalizado passando os parametros por **kwargs



### `generate_code()`

Irá retornar a string com a qual foi gerado o QRCode contendo os valores todos em suas posições como descrito na documentação do BACEN



## [Exemplos](./examples)

Contem mais exemplos para facilitar a sua implementação

1. [API](./examples/API/api.py) [Dockerfile - port 8000](./examples/API/Dockerfile)
1. [Console](./examples/console/console_example.py)

Em breve mais...

#### Toda contribuição é bem vinda!
