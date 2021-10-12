from setuptools import setup

with open("./README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='pixqrcode',
    version='1.0.3',
    description="QRCode Pix for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=['pixqrcode', 'pixqrcode.model', 'pixqrcode.utils', 'pixqrcode.service'],
    url='',
    license='',
    author='Joao Carlos',
    install_requires=[
        "qrcode"
    ],
    author_email='joao-mostela@hotmail.com',
)
