import pygame, os

BASE_IMAGE_PATH = ''

def set_path(path):
    BASE_IMAGE_PATH = path

def load_img(path):
    img = pygame.image.load(BASE_IMAGE_PATH + path).convert()
    img.set_colorkey((0, 0, 0))
    return img

def load_imgs(path):
    imgs = []
    for img_name in os.listdir(BASE_IMAGE_PATH + path):
        imgs.append(load_img(path + '/' + img_name))
    return imgs
