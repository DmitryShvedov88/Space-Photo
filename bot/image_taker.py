import os


def takeFiles():
    directory = "C:/Users/nivka/Desktop/Обучение Питон/Мои проекты/images"
    global name
    images = []
    try:
        filesindir = os.listdir(directory)
        for filesindirs in filesindir:
            name = os.path.join(filesindirs)
            path = os.path.join(str(directory), name)
            images.append(path)
        return images
    except Exception as exp:
        print(str(exp), "err")
