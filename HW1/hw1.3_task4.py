
# Name Surname: Emine Aydın
# ID: 190315053

from PIL import Image,ImageFilter

u = Image.open("C:/Users/Emine/Desktop/images/mandi/mandi.tif")
u.show()

u.save("C:/Users/Emine/Desktop/images/mandi/mandi2.tif")

u.rotate(180).save("C:/Users/Emine/Desktop/images/mandi/mandi3.tif")

u.convert(mode= "L").save("C:/Users/Emine/Desktop/images/mandi/mandi4.tif")

u.filter(ImageFilter.GaussianBlur(7)).save("C:/Users/Emine/Desktop/images/mandi/mandi5.tif")

resize = (960,600)
u.thumbnail(resize)
u.save("C:/Users/Emine/Desktop/images/mandi/mandi6.tif")

cut = (240,0,700,400)
u.crop(cut).save("C:/Users/Emine/Desktop/images/mandi/mandi7.tif")

