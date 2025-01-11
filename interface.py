from PyQt5.QtWidgets import QPushButton,QListWidget,QLabel,QApplication, QWidget, QHBoxLayout, QVBoxLayout, QMessageBox, QFileDialog, QSlider, QInputDialog, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
import os


app = QApplication([])

window = QWidget()
window.setFixedSize(750,600)
window.setWindowTitle("Easy Editor")

#ряд 1
folder = QPushButton("Папка")
photo_list = QListWidget()
photo_label = QLabel("Тіпа фотка")
right = QPushButton("Вправо")
left = QPushButton("Вліво")
mirror = QPushButton("Дзеркало")
blur = QPushButton("Замилення")
black_white = QPushButton("Ч/Б")
crop_range = QLineEdit()

#ряд 2
save_photo = QPushButton("Зберегти")
save_photo.setDisabled(True)
photo_crop = QPushButton("Обрізати")
photo_size = QPushButton("Розмір")
size_range = QLineEdit()
photo_rotate_range = QPushButton("Обернути")
Blur_range = QSlider(orientation=Qt.Orientation.Horizontal)
Blur_range.setMinimum(1)
Blur_range.setMaximum(100)

Rotate_range = QSlider(orientation=Qt.Orientation.Horizontal)
Rotate_range.setMinimum(1)
Rotate_range.setMaximum(360)

#Layout
blur_layout = QVBoxLayout()
blur_layout.addWidget(blur)
blur_layout.addWidget(Blur_range)

crop_layout = QVBoxLayout()
crop_layout.addWidget(photo_crop)
crop_layout.addWidget(crop_range)

size_layout = QVBoxLayout()
size_layout.addWidget(photo_size)
size_layout.addWidget(size_range)

rotate_layout = QVBoxLayout()
rotate_layout.addWidget(photo_rotate_range)
rotate_layout.addWidget(Rotate_range)

panel_layout_2 = QHBoxLayout()
panel_layout_2.addWidget(save_photo, stretch=1)
panel_layout_2.addLayout(crop_layout,stretch=1)
panel_layout_2.addLayout(size_layout, stretch=1)
#panel_layout_2.addWidget(Blur_range, stretch=1)
panel_layout_2.addLayout(rotate_layout, stretch=1)

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
base2_layout.addLayout(panel_layout_2)

base_layout = QHBoxLayout()
base_layout.addLayout(main_layout, stretch=1)
base_layout.addLayout(base2_layout, stretch= 4)
window.setLayout(base_layout)




