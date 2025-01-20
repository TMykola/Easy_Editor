from interface import *
from PIL import Image, ImageFilter

WIDTH, HEIGHT = photo_label.geometry().width(), photo_label.geometry().height()

def filter(all_obj):
    exp = [".jpeg", ".jpg", ".png", ".gif", ".bmp"]
    result = list()
    for file in all_obj:
        for ex in exp:
            if file.endswith(ex):
                result.append(file)
    return result

def error(txt):
    mb = QMessageBox()
    mb.setText(txt)
    mb.exec_()

def choose_workdir():
    global workdir, new_workdir
    workdir = QFileDialog.getExistingDirectory()
    new_workdir = workdir
    try:
        photo_list.addItems(filter(os.listdir(workdir)))
    except:
        error("Спочатку виберіть папку де наявні фотографії")

def show_photo():
    global name_photo, new_name_photo
    name_photo = photo_list.currentItem().text()
    new_name_photo = name_photo
    photo.load(os.path.join(workdir, name_photo))
    photo_label.setPixmap(photo.scaled(WIDTH,HEIGHT, aspectRatioMode=Qt.KeepAspectRatio))

def make_save():
    global workdir, name_photo
    workdir = new_workdir
    name_photo = new_name_photo

def make_left():
    global new_name_photo, new_workdir
    try:
        abs_path_photo = os.path.join(workdir,name_photo)
        new_workdir = os.path.join(os.path.abspath(__file__ + "/.."), "Image")
        new_name_photo = "left" + name_photo
        with Image.open(abs_path_photo) as photo_obj:
            photo_left = photo_obj.transpose(Image.ROTATE_90)
            new_abs_path_photo = os.path.join(new_workdir, new_name_photo)
            photo_left.save(new_abs_path_photo)
        photo.load(new_abs_path_photo)
        photo_label.setPixmap(photo.scaled(WIDTH,HEIGHT,aspectRatioMode=Qt.KeepAspectRatio))
    except:
        error("Спочатку виберіть фотографію")   

def make_right():
    global new_name_photo, new_workdir
    try:
        abs_path_photo = os.path.join(workdir,name_photo)
        new_workdir = os.path.join(os.path.abspath(__file__ + "/.."), "Image")
        new_name_photo = "right" + name_photo
        with Image.open(abs_path_photo) as photo_obj:
            photo_right = photo_obj.transpose(Image.ROTATE_270)
            new_abs_path_photo = os.path.join(new_workdir, new_name_photo)
            photo_right.save(new_abs_path_photo)
        photo.load(new_abs_path_photo)
        photo_label.setPixmap(photo.scaled(WIDTH,HEIGHT,aspectRatioMode=Qt.KeepAspectRatio))
    except:
        error("Спочатку виберіть фотографію")   

def make_blur():
    global new_name_photo, new_workdir
    try:
        abs_path_photo = os.path.join(workdir,name_photo)
        new_workdir = os.path.join(os.path.abspath(__file__ + "/.."), "Image")
        new_name_photo = "blur" + name_photo
        with Image.open(abs_path_photo) as photo_obj:
            photo_blur = photo_obj.filter(ImageFilter.GaussianBlur(Blur_range.value()))
            new_abs_path_photo = os.path.join(new_workdir, new_name_photo)
            photo_blur.save(new_abs_path_photo)
        photo.load(new_abs_path_photo)
        photo_label.setPixmap(photo.scaled(WIDTH,HEIGHT,aspectRatioMode=Qt.KeepAspectRatio))
    except:
        error("Спочатку виберіть фотографію")   

def make_bw():
    global new_name_photo, new_workdir
    try:
        abs_path_photo = os.path.join(workdir,name_photo)
        new_workdir = os.path.join(os.path.abspath(__file__ + "/.."), "Image")
        new_name_photo = "bw" + name_photo
        with Image.open(abs_path_photo) as photo_obj:
            photo_bw = photo_obj.convert("L")
            new_abs_path_photo = os.path.join(new_workdir, new_name_photo)
            photo_bw.save(new_abs_path_photo)
        photo.load(new_abs_path_photo)
        photo_label.setPixmap(photo.scaled(WIDTH,HEIGHT,aspectRatioMode=Qt.KeepAspectRatio))
    except:
        error("Спочатку виберіть фотографію")   

def make_mirorr():
    global new_name_photo, new_workdir
    try:
        abs_path_photo = os.path.join(workdir,name_photo)
        new_workdir = os.path.join(os.path.abspath(__file__ + "/.."), "Image")
        new_name_photo = "mirorr" + name_photo
        with Image.open(abs_path_photo) as photo_obj:
            photo_mirorr = photo_obj.transpose(Image.FLIP_LEFT_RIGHT)
            new_abs_path_photo = os.path.join(new_workdir, new_name_photo)
            photo_mirorr.save(new_abs_path_photo)
        photo.load(new_abs_path_photo)
        photo_label.setPixmap(photo.scaled(WIDTH,HEIGHT,aspectRatioMode=Qt.KeepAspectRatio))
    except:
        error("Спочатку виберіть фотографію") 

def make_crop():
    global new_name_photo, new_workdir
    try:
        abs_path_photo = os.path.join(workdir,name_photo)
        new_workdir = os.path.join(os.path.abspath(__file__ + "/.."), "Image")
        new_name_photo = "crop" + name_photo
        with Image.open(abs_path_photo) as photo_obj:
            crop_value = int(crop_range.text())
            photo_crop = photo_obj.crop((0, 0, crop_value, crop_value))
            new_abs_path_photo = os.path.join(new_workdir, new_name_photo)
            photo_crop.save(new_abs_path_photo)
        photo.load(new_abs_path_photo)
        photo_label.setPixmap(photo.scaled(WIDTH,HEIGHT,aspectRatioMode=Qt.KeepAspectRatio))
    except:
        error("Спочатку виберіть фотографію")   

def make_rotation():
    global new_name_photo, new_workdir
    try:
        abs_path_photo = os.path.join(workdir,name_photo)
        new_workdir = os.path.join(os.path.abspath(__file__ + "/.."), "Image")
        new_name_photo = "rotation" + name_photo
        with Image.open(abs_path_photo) as photo_obj:
            photo_rotation = photo_obj.rotate(Rotate_range.value())
            new_abs_path_photo = os.path.join(new_workdir, new_name_photo)
            photo_rotation.save(new_abs_path_photo)
        photo.load(new_abs_path_photo)
        photo_label.setPixmap(photo.scaled(WIDTH,HEIGHT,aspectRatioMode=Qt.KeepAspectRatio))
    except:
        error("Спочатку виберіть фотографію") 

def make_size():
    global new_name_photo, new_workdir
    try:
        abs_path_photo = os.path.join(workdir,name_photo)
        new_workdir = os.path.join(os.path.abspath(__file__ + "/.."), "Image")
        new_name_photo = "size" + name_photo
        with Image.open(abs_path_photo) as photo_obj:
            size_range_value = int(size_range.text())
            size_range_value1 = int(size_range1.text())
            photo_size = photo_obj.crop((0, 0, size_range_value, size_range_value1))
            new_abs_path_photo = os.path.join(new_workdir, new_name_photo)
            photo_size.save(new_abs_path_photo)
        photo.load(new_abs_path_photo)
        photo_label.setPixmap(photo.scaled(WIDTH,HEIGHT,aspectRatioMode=Qt.KeepAspectRatio))
    except:
        error("Спочатку виберіть фотографію") 

photo_size.clicked.connect(make_size)
photo_rotate.clicked.connect(make_rotation)
photo_crop.clicked.connect(make_crop)
save_photo.clicked.connect(make_save)
blur.clicked.connect(make_blur)
black_white.clicked.connect(make_bw)
mirror.clicked.connect(make_mirorr)
left.clicked.connect(make_left)
right.clicked.connect(make_right)
folder.clicked.connect(choose_workdir)
photo_list.clicked.connect(show_photo)

window.show()
app.exec_()
