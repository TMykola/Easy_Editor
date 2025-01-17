from PyQt5.QtWidgets import QPushButton,QListWidget,QLabel,QApplication, QWidget, QHBoxLayout, QVBoxLayout, QMessageBox, QFileDialog, QSlider, QInputDialog, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import os


app = QApplication([])

window = QWidget()
window.setFixedSize(750,600)
window.setWindowTitle("Easy Editor")

folder = QPushButton("Папка")
photo_list = QListWidget()
photo_label = QLabel("Тіпа фотка")
right = QPushButton("Вправо")
left = QPushButton("Вліво")
mirror = QPushButton("Дзеркало")
blur = QPushButton("Замилення")
black_white = QPushButton("Ч/Б")
Blur_range = QSlider(orientation=Qt.Orientation.Horizontal)
Blur_range.setMinimum(1)
Blur_range.setMaximum(100)


blur_layout = QVBoxLayout()
blur_layout.addWidget(blur)
blur_layout.addWidget(Blur_range)

panel_layout = QHBoxLayout()
panel_layout.addWidget(right, stretch=1)
panel_layout.addWidget(left, stretch=1)
panel_layout.addWidget(mirror, stretch=1)
panel_layout.addLayout(blur_layout, stretch=1)
panel_layout.addWidget(black_white, stretch=1)

photo = QPixmap()

main_layout = QVBoxLayout()
main_layout.addWidget(folder, stretch=1)
main_layout.addWidget(photo_list, stretch=3)

base2_layout = QVBoxLayout()
base2_layout.addWidget(photo_label, stretch=4, alignment= Qt.AlignCenter)
base2_layout.addLayout(panel_layout)

base_layout = QHBoxLayout()
base_layout.addLayout(main_layout, stretch=1)
base_layout.addLayout(base2_layout, stretch= 4)
window.setLayout(base_layout)


