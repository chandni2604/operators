import pyqrcode
import png


try:
    j='world'
    url=pyqrcode.create(j)
    url.png('D:/Images/world.png',scale=4)
    print('your png created')
except Exception as e:
    print(e)
