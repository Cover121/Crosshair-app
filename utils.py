import urllib.request
from PyQt5 import QtGui

def get_pixmap_from_url(url):
    data = urllib.request.urlopen(url).read()
    image = QtGui.QImage()
    image.loadFromData(data)
    return QtGui.QPixmap(image)
