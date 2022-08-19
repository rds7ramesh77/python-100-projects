#You need to install one python library ie: pyqrcode as pip install pyqrcode
import pyqrcode
from pyqrcode import QRCode

#String which represent the QR code

s="https://www.sapkotaramesh.com.np"

url=pyqrcode.create(s)
url.svg("mywebsite.svg",scale=10) 