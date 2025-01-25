import os
from PyQt5.QtGui import QIcon, QPixmap

def load_icon(icon_name):
    icon_path = os.path.join(os.path.dirname(__file__), 'resources', icon_name)
    return QIcon(icon_path)

def load_pixmap(image_name):
    image_path = os.path.join(os.path.dirname(__file__), 'resources', image_name)
    return QPixmap(image_path)
