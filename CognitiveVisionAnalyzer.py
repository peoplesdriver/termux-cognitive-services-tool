#! /usr/bin/python

# Tool to analyze images and get a description
#  TODO  better description snd comments
from helpers import*
from vision_tools import local_img_analyzer, remote_img_analyzer
from scraper import scraper
import time

header()

menu1 = ["Please choose to analyze images from:",\
         "\t1. Local file disk.",\
         "\t2. Remote location URL",\
         "\t3. Exit"]

menu_option1 = ["Options:",\
                "\t1. Download to './images'",\
                "\t2. Analyze from './images'",\
                "\t3. Return to main menu."]

def user_menu(menu,menu_option):
    user_input = get_user_input(menu)
    if (user_input == 1):
        header()
        user_input = get_user_input(menu_option)
        if (user_input == 1):
            header()
            try:
                web_url = input("Please enter website address URL >>> ")            #  scrap website for images and download them in images folder in home directory
                header()
                ftype = input("Enter file format(ex.'.jpg','.png','txt') >>> ")
                scraper(web_url)
                print("Download complete")
                time.sleep(3)
                header()
                user_input = -1
                user_menu(menu, menu_option)

            except:
                header()
                print ("Errors encountered")

            finally:
                header()
                user_input = -1
                user_menu(menu, menu_option)

        elif (user_input == 2):
            local_file_list = get_local_file_list('images',ftype)

            for i in range(len(local_file_list)):
               local_image_path = local_file_list[i]
               local_img_analyzer(local_image_path)
               time.sleep(5)
            header()
            user_input = -1
            user_menu(menu, menu_option)

        elif (user_input == 3):
            header()
            user_input = -1
            user_menu(menu,menu_option)

        else:
            print ("Please enter option 1, 2 or 3")
            header()
            get_user_input(menu_option)
#TODO

    elif (user_input == 2):
        try:
            web_url = input("Please enter website address URL >>> ")
            link_list = scraper(web_url).copy()
            header()
            for i in range(len(link_list)):
                link_url = str(link_list[i])
                remote_img_analyzer(link_url)
                time.sleep(5)
            header()
            user_input = -1
            user_menu(menu,menu_option)

        except :
            header()
            print(f"Something wrong: {link_list[i]}")

#        finally:
#            header()
#            user_input = -1
#            user_menu(menu,menu_option)

    elif (user_input == 3):
        sys.exit()
        #  exit program

    else:
        header()
        print(" Please enter option 1 or 2. ")
        user_menu(menu,menu_option)


user_menu(menu1,menu_option1)
