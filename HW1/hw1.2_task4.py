
# Name Surname: Emine Aydın
# ID: 190315053

from PIL import Image,ImageFilter

u = Image.open("C:/Users/Emine/Desktop/images/Lighthouse/lighthouse.png")
u.show()

u.save("C:/Users/Emine/Desktop/images/Lighthouse/lighthouse2.png")

u.rotate(180).save("C:/Users/Emine/Desktop/images/Lighthouse/lighthouse3.png")

u.convert(mode= "L").save("C:/Users/Emine/Desktop/images/Lighthouse/lighthouse4.png")

u.filter(ImageFilter.GaussianBlur(5)).save("C:/Users/Emine/Desktop/images/Lighthouse/lighthouse5.png")

resize = (960,600)
u.thumbnail(resize)
u.save("C:/Users/Emine/Desktop/images/Lighthouse/lighthouse6.png")

cut = (240,0,700,400)
u.crop(cut).save("C:/Users/Emine/Desktop/images/Lighthouse/lighthouse7.png")