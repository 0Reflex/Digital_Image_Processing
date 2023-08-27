
# Name Surname: Emine Aydın
# ID: 190315053

from PIL import Image,ImageFilter

u = Image.open("C:/Users/Emine/Desktop/images/Blobs/blobs.png")
u.show()


u.save("C:/Users/Emine/Desktop/images/Blobs/blobs2.png")

u.rotate(180).save("C:/Users/Emine/Desktop/images/Blobs/blobs3.png")

u.convert(mode= "L").save("C:/Users/Emine/Desktop/images/Blobs/blobs4.png")

u = u.convert('RGB')
u = u.filter(ImageFilter.BLUR)
u.save("C:/Users/Emine/Desktop/images/Blobs/blobs7.png")

resize = (90,600)
u.thumbnail(resize)
u.save("C:/Users/Emine/Desktop/images/Blobs/blobs5.png")


cut = (40,0,300,200)
u.crop(cut).save("C:/Users/Emine/Desktop/images/Blobs/blobs6.png")








