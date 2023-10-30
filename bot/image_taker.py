import os


def takefiles(directory):
    images = []
    filesindir = os.listdir(directory)
    for filesindirs in filesindir:
        name = os.path.join(filesindirs)
        path = os.path.join(str(directory), name)
        images.append(path)
    return images
