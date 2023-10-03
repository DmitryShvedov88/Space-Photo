import os
import argparse


def takeFiles():
    directory = "C:/Users/nivka/Desktop/Обучение Питон/Мои проекты/images"
    global file, name
    images=[]
    try:
        filesindir = os.listdir(directory)
        #print(filesindir)
        for filesindirs in filesindir:
            #print(filesindirs)
            name = os.path.join(filesindirs)
            path = os.path.join(str(directory), name)
            images.append(path)        
        #     func(True)
        # nm.lineEdit.clear()
        # ui.lineEdit.clear()
        # ui.lineEdit_2.clear()
        return images
    except Exception as exp:
        print(str(exp), "err")
