import os

import pygame

BASE_IMG_PATH = 'data/images/'

def load_image(path):
    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    img.set_colorkey((0, 0, 0))
    return img

def load_images(path):
    images = []
    for img_name in sorted(os.listdir(BASE_IMG_PATH + path)):
        images.append(load_image(path + '/' + img_name))
    return images
class Animation:
    def __init__(self,images,img_dur=5,loop=True):
        self.images=images
        self.image_duration=img_dur
        self.loop=loop
        self.frame=0
        self.done=False

    def copy(self):
        return Animation(self.images,self.image_duration,self.loop)
    def update(self):
        if self.loop:
            self.frame=(self.frame+1) % (self.image_duration * len(self.images))
        else:
            self.frame=min(self.frame+1,self.image_duration*len(self.images))
            if self.frame>=self.image_duration*len(self.images):
                self.done=True
    def img(self):
        return self.images[int(self.frame / self.image_duration)]

        