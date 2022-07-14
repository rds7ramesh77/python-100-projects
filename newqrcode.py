#four line qr code 

import qrcode 
img=qrcode.make(
    "https://www.sapkotaramesh.com.np"
)
img.save("myQR.png")
img.show()