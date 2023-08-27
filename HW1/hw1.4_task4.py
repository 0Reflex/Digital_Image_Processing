
# Name Surname: Emine Aydın
# ID: 190315053

from PIL import Image,ImageFilter

u = Image.open("C:/Users/Emine/Desktop/images/Shadow/shadow.tif")
u.show()

u.save("C:/Users/Emine/Desktop/images/Shadow/shadow2.tif")

u.rotate(180).save("C:/Users/Emine/Desktop/images/Shadow/shadow3.tif")

u.convert(mode= "L").save("C:/Users/Emine/Desktop/images/Shadow/shadow4.tif")

u = u.convert('RGB')
u = u.filter(ImageFilter.BLUR)
u.save("C:/Users/Emine/Desktop/images/Shadow/shadow7.tif")

resize = (60,600)
u.thumbnail(resize)
u.save("C:/Users/Emine/Desktop/images/Shadow/shadow5.tif")

cut = (40,0,300,200)
u.crop(cut).save("C:/Users/Emine/Desktop/images/Shadow/shadow6.tif")



