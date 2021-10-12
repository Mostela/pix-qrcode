from typing import Optional
from pixqrcode import PixQrCode

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Pix(BaseModel):
    name: str
    mobile: str
    city: str
    price: float


@app.post("/")
async def generate_qrcode(pix: Pix):
    return PixQrCode(pix.name, pix.mobile, pix.city, str(pix.price)).export_base64()
