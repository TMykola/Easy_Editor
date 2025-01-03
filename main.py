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
        
def make_right():
    abs_path_photo = os.path.join(workdir,name_photo)
    with Image.open(abs_path_photo) as photo_obj:
        photo_right = photo_obj.transpose(Image.ROTATE_270)
        new_abs_path_photo = os.path.join(workdir, "Image", "right_" + name_photo)
        photo_right.save(new_abs_path_photo)
    photo.load(new_abs_path_photo)
    photo_label.setPixmap(photo.scaled(WIDTH,HEIGHT,aspectRatioMode=Qt.KeepAspectRatio))

def make_miror():
    abs_path_photo = os.path.join(workdir,name_photo)
    with Image.open(abs_path_photo) as photo_obj:
        photo_miror = photo_obj.transpose(Image.FLIP_LEFT_RIGHT)
        new_abs_path_photo = os.path.join(workdir, "Image", "miror_" + name_photo)
        photo_miror.save(new_abs_path_photo)
    photo.load(new_abs_path_photo)
    photo_label.setPixmap(photo.scaled(WIDTH,HEIGHT,aspectRatioMode=Qt.KeepAspectRatio))

def make_black_white():
    abs_path_photo = os.path.join(workdir,name_photo)
    with Image.open(abs_path_photo) as photo_obj:
        photo_BW = photo_obj.convert("L")
        new_abs_path_photo = os.path.join(workdir, "Image", "BW_" + name_photo)
        photo_BW.save(new_abs_path_photo)
    photo.load(new_abs_path_photo)
    photo_label.setPixmap(photo.scaled(WIDTH,HEIGHT,aspectRatioMode=Qt.KeepAspectRatio))

def make_blur():
    pass

blur.clicked.connect(make_blur)
black_white.clicked.connect(make_black_white)
mirror.clicked.connect(make_miror)
left.clicked.connect(make_left)
right.clicked.connect(make_right)
folder.clicked.connect(choose_workdir)
photo_list.clicked.connect(show_photo)

window.show()
app.exec_()
