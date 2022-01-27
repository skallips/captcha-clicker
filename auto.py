# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 13:00:32 2021

@author: brian
"""
import pyautogui as pt
import requests as req
from bs4 import BeautifulSoup as bs
from os import listdir
from os.path import isfile, join

class Clicker:
    def __init__(self, target):
        self.target = target
        pt.FAILSAFE = True

    def nav_to_image(self):
        try:
            positionX, positionY = pt.locateCenterOnScreen(self.target, confidence=.8)  
            pt.Click(positionX, positionY)

        except:
            print('No image found...')
            return 0

class FindImages:
    def setImages(self, mypath, url):
        count = 0
        r = req.get(url)
        soup =  bs(r.text, 'html.parser')    
        images = soup.findAll('img')
        if len(images) != 0:
            try:
                image_link = images["data-srcset"]
            except:
                try:
                    image_link = images["data-src"]
                except:
                    try:
                        image_link = images["data-fallback-src"]
                    except:
                        try:
                            image_link = images["src"]
                        except:
                            print('no images in url')
                            pass
            try:
                r = req.get(image_link).content
                try:
                    r = str(r, 'utf-8')
                except UnicodeDecodeError:
                    with open(f"{mypath}/images{i+1}.jpg", "wb+") as f:
                        f.write(r)
                    count += 1
            except:
                pass
    def getImages(self, mypath):
        onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
        return onlyfiles
        
if __name__ == '__auto__':
    url = ''
    FindImages.setImages('images', url)
    files = FindImages.getImages('images')
    for i in files:
        clicker = Clicker(i)
        while(True):
            w = url
            