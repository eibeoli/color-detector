import random
from py3pin.Pinterest import Pinterest
import requests

#initialize api
account = Pinterest(email='', password='', username='', cred_root='cred_root')

def search(query, max_items, scope='pins'): #return dict of imgs
    #valid_img = { ".jpg", ".png", ".gif"}
    results = []
    print("test")
    search_batch = account.search(scope=scope, query=query)
    while len(search_batch) > 0 and len(results) < max_items:
        for x in search_batch:
            if 'images' not in x:
                continue
            if 'is_promoted' in x and (x['is_promoted'] is True):
                continue
            results.append({
                'link' : x['images']['orig']['url']
            })
    return results
