import qrcode
from PIL import Image, ImageDraw, ImageOps

logo_url = ".\\img\\logo.jpg"

logo = Image.open(logo_url)

base_width = 100

wpercent = (base_width/float(logo.size[0]))
hsize = int((float(logo.size[1])*float(wpercent)))
logo = logo.resize((base_width, hsize), Image.LANCZOS)


mask = Image.new("L", logo.size, 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0, logo.size[0], logo.size[1]), fill=255)
 
rounded_logo = ImageOps.fit(logo, mask.size, centering=(0.5, 0.5))
rounded_logo.putalpha(mask)

QRcode = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
)
url = "https://leonardo2322.github.io/Palerossi/"

QRcode.add_data(url)

QRcode.make()

QRcolor = "#000000"

QRimg = QRcode.make_image(
    fill_color=QRcolor, back_color="white").convert('RGB')

pos = ((QRimg.size[0] - rounded_logo.size[0]) // 2,
       (QRimg.size[1] - rounded_logo.size[1]) // 2)

QRimg.paste(rounded_logo, pos, rounded_logo)
QRimg.save('URlPage.png')