import pyqrcode
from pyqrcode import QRCode

s="https://www.geeksforgeeks.org/working-on-git-bash/"

url=pyqrcode.create(s)

url.svg("GFGQRCode.svg",scale=8)