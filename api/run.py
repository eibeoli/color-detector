# get search term from api
# return colors + image
# detect: make_histogram, make_bar, sort_hsvs // scrape: search
import random
import urllib.request
import cv2
import numpy as np
from sklearn.cluster import KMeans
import scrape, detect

def run(input):

    modifier = ["aesthetic", "cute", "edit", "tumblr", "glitch", "photography"]
    if random.random() > .01:
        input += " " + random.choice(modifier)

    pictures = scrape.search(input, 10) #run search

    picture = random.choice(pictures)

    pic_str = str(picture['link']) #obtain image link

    return pic_str