from interface import *
from PIL import Image

WIDTH, HEIGHT = photo_label.geometry().width(), photo_label.geometry().height()



def filter(all_obj):
    exp = [".jpeg", ".jpg", ".png", ".gif", ".bmp"]
    result = list()
    for file in all_obj:
        for ex in exp:
            if file.endswith(ex):
                result.append(file)

    return result

def choose_workdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
    photo_list.addItems(filter(os.listdir()))

def show_photo():
    global name_photo
    name_photo = photo_list.currentItem().text()
    photo.load(os.path.join(workdir, name_photo))
    photo_label.setPixmap(photo.scaled(WIDTH,HEIGHT, aspectRatioMode=Qt.KeepAspectRatio))

def make_left():
    abs_path_photo = os.path.join(workdir,name_photo)
    with Image.open(abs_path_photo) as photo_obj:
        photo_left = photo_obj.transpose(Image.ROTATE_90)
        new_abs_path_photo = os.path.join(workdir, "Image", "left_" + name_photo)
        photo_left.save(new_abs_path_photo)
    photo.load(new_abs_path_photo)
    photo_label.setPixmap(photo.scaled(WIDTH,HEIGHT,aspectRatioMode=Qt.KeepAspectRatio))
        
left.clicked.connect(make_left)
folder.clicked.connect(choose_workdir)
photo_list.clicked.connect(show_photo)

window.show()
app.exec_()
