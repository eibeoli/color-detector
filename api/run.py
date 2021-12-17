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

    #now extract colors and return two as map duo to api
    #call functions here
    #make a map/hash of colors and image, return

    # START HERE
    retrieve_img = urllib.request.urlretrieve(pic_str, "local.jpg")
    img = cv2.imread("local.jpg")
    #height, width, _ = np.shape(img)

    # reshape the image to be a simple list of RGB pixels
    #image = img.reshape((height * width, 3))

    # we'll pick the 5 most common colors
    #num_clusters = 5
    #clusters = KMeans(n_clusters=num_clusters)
    #clusters.fit(image)

    # count the dominant colors and put them in "buckets"
    #histogram = detect.make_histogram(clusters)
    # then sort them, most-common first
    #combined = zip(histogram, clusters.cluster_centers_)
    #combined = sorted(combined, key=lambda x: x[0], reverse=True)

    # finally, we'll output a graphic showing the colors in order
    #bars = []
    #hsv_values = []
    #colors = []
    #for index, rows in enumerate(combined):
    #    bar, rgb, hsv = detect.make_bar(100, 100, rows[1])
    #    colors.append(rgb)
    #    #print(f'Bar {index + 1}')
    #    #print(f'  RGB values: {rgb}')
    #    #print(f'  HSV values: {hsv}')
    #    hsv_values.append(hsv)
    #    bars.append(bar)

    # sort the bars[] list so that we can show the colored boxes sorted
    # by their HSV values -- sort by hue, then saturation
    #sorted_bar_indexes = detect.sort_hsvs(hsv_values)
    #sorted_bars = [bars[idx] for idx in sorted_bar_indexes]

    #colors = np.vstack(bars).tolist()

    #save colors as array of 5 rgb things
    
    #get array of rbg colors

    #pack = {
    #    "image" : "local.jpg", #return img or link?
    #    "colors" : colors #this isnt coming out correctly, mayb just store rgb + display over js
    #}
    

    #cv2.imshow('Sorted by HSV values', np.vstack(sorted_bars))
    #cv2.imshow(f'{num_clusters} Most Common Colors', np.vstack(bars))
    #cv2.waitKey(0)

    return pic_str