from PyQt5 import QtCore, QtGui, QtWidgets

class CrosshairOverlay(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(
            QtCore.Qt.FramelessWindowHint |
            QtCore.Qt.WindowStaysOnTopHint |
            QtCore.Qt.X11BypassWindowManagerHint |
            QtCore.Qt.Tool
        )
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setAttribute(QtCore.Qt.WA_NoSystemBackground, True)
        self.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)

        self.crosshair_size = 20
        self.crosshair_color = QtGui.QColor(255, 0, 0)
        self.crosshair_type = 'circle'  # default
        self.visible = True
        self.screen_geometry = QtWidgets.QApplication.primaryScreen().geometry()
        self.resize(self.screen_geometry.width(), self.screen_geometry.height())
        self.showFullScreen()

    def toggle_visibility(self):
        self.visible = not self.visible
        self.update()

    def set_crosshair_size(self, size):
        self.crosshair_size = size
        self.update()

    def set_crosshair_type(self, crosshair_type):
        self.crosshair_type = crosshair_type.lower()
        self.update()

    def set_crosshair_color(self, color):
        self.crosshair_color = color
        self.update()

    def paintEvent(self, event):
        if not self.visible:
            return

        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        center = QtCore.QPoint(self.screen_geometry.width() // 2, self.screen_geometry.height() // 2)

        if self.crosshair_type == 'circle':
            pen = QtGui.QPen(self.crosshair_color, 2)
            painter.setPen(pen)
            painter.setBrush(QtCore.Qt.NoBrush)
            painter.drawEllipse(center, self.crosshair_size, self.crosshair_size)
        elif self.crosshair_type == '+':
            pen = QtGui.QPen(self.crosshair_color, 2)
            painter.setPen(pen)
            length = self.crosshair_size
            painter.drawLine(center.x() - length, center.y(), center.x() + length, center.y())
            painter.drawLine(center.x(), center.y() - length, center.x(), center.y() + length)
        elif self.crosshair_type == 'dot':
            painter.setPen(QtCore.Qt.NoPen)
            painter.setBrush(QtGui.QBrush(self.crosshair_color))
            dot_size = max(1, self.crosshair_size)
            painter.drawEllipse(center, dot_size // 2, dot_size // 2)
