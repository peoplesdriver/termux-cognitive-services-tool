#! /usr/bin/python

#  scraper

import os
import requests
import sys
import shutil
import re
import threading
from bs4 import BeautifulSoup as soup

THREAD_COUNTER = 0  # set thread counter to 0
THREAD_MAX     = 5  # set max thread to 5

# function to get the source of website 
def get_source( link ):
    response = requests.get( link )
    #  if response OK/200 return soup object
    if response.status_code == 200:
        return soup( response.text,features="lxml" )
    else:
        sys.exit( " Invalid Response Received." )

#  function to filter just the img tags
def filter( html ):
    imgs = html.findAll( "img" )
    if imgs:
        return imgs
    else:
        sys.exit(" No images detected on the page.")

#  function to handle the request response
def requesthandle( link, name ):
    global THREAD_COUNTER
    THREAD_COUNTER += 1
    try:
        #  check if folder images exist in home directory
        if not os.path.exists('images'):
            #  create folder directory images
            os.mkdir( os.path.join( os.getcwd(), 'images' ) )
        
        response = requests.get( link, stream=True )
        if response.status_code == 200:
            response.raw.decode_content = True
            #  create file in ./images folder
            file = open( './images/' + name, "wb" )
            shutil.copyfileobj(response.raw, file)
            file.close()
#            print(f" Downloaded Image: {name}")
    except Exception:
        print (f" Error Occured with {name}")

    THREAD_COUNTER -= 1

#  main function to scrap a website for jpg/png type file
#  and download them to ./images folder
def scraper(web_url):

    link_list = []

    #  check if the url is prepended by http
    if not web_url.startswith("http"):
        web_url = "https://" + web_url
    #  compile regex to search for
    regex = re.compile(r"((?:https?:\/\/.*)?\/(.*\.(?:jpg)))")

    html = get_source(web_url)
    tags = filter(html)
    for tag in tags:
        src = tag.get("src")
        if src:
            src = re.match( regex, src )
            if src:
                (link, name) = src.groups()
                #  check if url starts with http
#              print(link)
#                if not link.startswith("http"):
#                    link = "https://" + link
                link_list.append(link)

                _t = threading.Thread( target=requesthandle, args=(link, name.split("/")[-1]) )
                _t.daemon = True
                _t.start()

                while THREAD_COUNTER >= THREAD_MAX:
                    pass
    return link_list

    while THREAD_COUNTER > 0:
        pass


# test 

#temp = scraper('www.drivespark.com')

#for i in range(len(temp)):
#    print(str(i) +' '+ temp[i])


