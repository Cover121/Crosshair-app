from PyQt5 import QtCore, QtGui, QtWidgets
from utils import get_pixmap_from_url

class ControlWindow(QtWidgets.QWidget):
    def __init__(self, overlay):
        super().__init__()
        self.overlay = overlay
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Crosshair by Cover")
        self.setFixedSize(300, 320)
        self.setWindowIcon(QtGui.QIcon(get_pixmap_from_url("https://i.ibb.co/kgBpHnPp/pngtree-crosshair-icon-isolated-on-abstract-background-png-image-1875387.jpg")))

        # Set background image
        background = get_pixmap_from_url("https://i.ibb.co/kgth3zC7/bg-kv.jpg")
        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Background, QtGui.QBrush(background.scaled(self.size(), QtCore.Qt.IgnoreAspectRatio)))
        self.setPalette(palette)

        layout = QtWidgets.QVBoxLayout()

        self.toggle_button = QtWidgets.QPushButton("Toggle Crosshair")
        self.toggle_button.clicked.connect(self.overlay.toggle_visibility)

        self.size_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.size_slider.setMinimum(5)
        self.size_slider.setMaximum(100)
        self.size_slider.setValue(self.overlay.crosshair_size)
        self.size_slider.valueChanged.connect(self.overlay.set_crosshair_size)

        self.crosshair_selector = QtWidgets.QComboBox()
        self.crosshair_selector.addItems(['Circle', '+', 'Dot'])
        self.crosshair_selector.currentTextChanged.connect(self.overlay.set_crosshair_type)

        self.color_button = QtWidgets.QPushButton("Choose Color")
        self.color_button.clicked.connect(self.choose_color)

        self.copyright_label = QtWidgets.QLabel("© Creator Cover 2025 - All Rights Reserved")
        self.copyright_label.setAlignment(QtCore.Qt.AlignCenter)
        self.setStyleSheet("QLabel { color: white; font-size: 10px; }")

        layout.addWidget(self.toggle_button)
        layout.addWidget(QtWidgets.QLabel("Crosshair Size"))
        layout.addWidget(self.size_slider)
        layout.addWidget(QtWidgets.QLabel("Crosshair Type"))
        layout.addWidget(self.crosshair_selector)
        layout.addWidget(QtWidgets.QLabel("Crosshair Color"))
        layout.addWidget(self.color_button)
        layout.addStretch()
        layout.addWidget(QtWidgets.QLabel())
        layout.addWidget(self.copyright_label)

        self.setLayout(layout)
        self.show()

    def choose_color(self):
        color = QtWidgets.QColorDialog.getColor()
        if color.isValid():
            self.overlay.set_crosshair_color(color)
