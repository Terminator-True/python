from shutil import rmtree
import random
import os
import re
from instagram_private_api.endpoints import upload
from instaloader.instaloader import Instaloader
from instaloader.structures import Profile
from requests import sessions
from requests.sessions import session
import instaloader
import datetime
import autoit
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from numpy import concatenate
L=Instaloader()


def download(profile):
    i=0
    for post in profile.get_posts():
        L.download_post(post, target=profile.username)
        i+=1
        if i==15:
            break

def CuentaRandom():
    with open("Fotos\Cuentas.txt","r") as f:
        x = f.read()
        cuentas=x.split("\n")
    return cuentas[random.randint(0,len(cuentas)-1)]

def textGenerator():
    with open("Fotos\Frases.txt","r") as f:
        frases = f.readlines()
    return frases[random.randint(0,len(frases)-1)]

def UploadFoto(Nombre):
    username = "bromacibernetica2" #Enter your username
    password = "ShitPost4,2" #Enter your password
    dirpath = os.chdir(Nombre)
    files = os.listdir(dirpath)
    regex = re.compile(r".jpg")
    filtered_files = list(filter(regex.search, files))
    image_path = "C:\\Users\\jf28r\\Desktop\\python\\"
    image_path += Nombre+"\\"+filtered_files[random.randint(0,len(filtered_files)-1)] 
    caption = textGenerator() #Enter the caption 

    mobile_emulation = { "deviceName": "Pixel 2" }
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("mobileEmulation", mobile_emulation)

    driver = webdriver.Chrome(executable_path=r"C:\\Users\\jf28r\\Desktop\\python\\chromedriver.exe",options=opts) #you must enter the path to your driver

    main_url = "https://www.instagram.com/?hl=en-gb"
    driver.get(main_url)

    sleep(4)

    def login():
        driver.find_element_by_xpath("//button[text()='Accept All']").click()
        sleep(3)
        login_button = driver.find_element_by_xpath("//button[contains(text(),'Log In')]")
        login_button.click()
        sleep(3)
        username_input = driver.find_element_by_xpath("//input[@name='username']")
        username_input.send_keys(username)
        password_input = driver.find_element_by_xpath("//input[@name='password']")
        password_input.send_keys(password)
        password_input.submit()

    login()

    sleep(4)

    def close_reactivated():
        try:
            sleep(2)
            not_now_btn = driver.find_element_by_xpath("//a[contains(text(),'Not Now')]")
            not_now_btn.click()
        except:
            pass

    close_reactivated()

    def close_notification():
        try: 
            sleep(2)
            close_noti_btn = driver.find_element_by_xpath("//button[contains(text(),'Not Now')]")
            close_noti_btn.click()
            sleep(2)
        except:
            pass

    close_notification()

    def close_add_to_home():
        sleep(3) 
        close_addHome_btn = driver.find_element_by_xpath("//button[contains(text(),'Cancel')]")
        close_addHome_btn.click()
        sleep(1)

    close_add_to_home()

    sleep(3)

    close_notification()

    new_post_btn = driver.find_element_by_xpath("//div[@role='menuitem']").click()
    sleep(1.5)
    autoit.win_active("Abrir") 
    sleep(5)
    autoit.control_send("Abrir","Edit1",image_path) 
    sleep(1.5)
    autoit.control_send("Abrir","Edit1","{ENTER}")

    sleep(2)

    next_btn = driver.find_element_by_xpath("//button[contains(text(),'Siguiente')]").click()

    sleep(1.5)

    caption_field = driver.find_element_by_xpath("//textarea[@aria-label='Escribe un pie de foto o vídeo...']")
    caption_field.send_keys(caption)

    share_btn = driver.find_element_by_xpath("//button[contains(text(),'Compartir')]").click()

    sleep(25)

    driver.close()
    
def borraRastro(Nombre):
    rmtree("C:\\Users\\jf28r\\Desktop\\python\\"+Nombre)

def programaPrincipal():
    try:
        Nombre=CuentaRandom()
        profile=Profile.from_username(L.context,Nombre)
        download(profile)
        UploadFoto(Nombre)
        borraRastro(Nombre)
        return True
    except:
        return False

"""
acabat = False
while acabat is not True:
    if programaPrincipal():
        sleep(7200)
    else:
        acabat = False
"""
borraRastro(Nombre="ofenderse")
