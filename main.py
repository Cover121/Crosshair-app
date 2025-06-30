import sys
from PyQt5 import QtWidgets
from overlay import CrosshairOverlay
from control_window import ControlWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    overlay = CrosshairOverlay()
    control = ControlWindow(overlay)
    sys.exit(app.exec_())
