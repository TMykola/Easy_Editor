from PyQt5.QtWidgets import QPushButton,QListWidget,QLabel,QApplication, QWidget, QHBoxLayout, QVBoxLayout

app = QApplication([])

window = QWidget()
window.setFixedSize(700,600)
window.setWindowTitle("Easy Editor")

folder = QPushButton("Папка")
photo_list = QListWidget()
photo_place = QLabel("Тіпа фотка")
right = QPushButton("Вправо")
left = QPushButton("Вліво")
mirror = QPushButton("Дзеркало")
sharpness = QPushButton("Різкість")
black_white = QPushButton("Ч/Б")


panel_layout = QHBoxLayout()
panel_layout.addWidget(right)
panel_layout.addWidget(left)
panel_layout.addWidget(mirror)
panel_layout.addWidget(sharpness)
panel_layout.addWidget(black_white)

main_layout = QVBoxLayout()
main_layout.addWidget(folder, stretch=1)
main_layout.addWidget(photo_list, stretch=3)

base_layout = QHBoxLayout()
base_layout.addLayout(main_layout, stretch=1)
base_layout.addWidget(photo_place, stretch=4)

base2_layout = QVBoxLayout()
base2_layout.addLayout(base_layout)
base2_layout.addLayout(panel_layout)

window.setLayout(base2_layout)




window.show()
app.exec_()
