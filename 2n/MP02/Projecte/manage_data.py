import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
def connect():
    with MongoClient('localhost',27017,username='Joel_r',password='Admin@123',authSource='JoelFarell') as client:
        return client

def filtra_str(string):
    return string.replace(" ","").replace("\n","")
def filtra_img(img):
    return img.replace("(","").replace(")","").replace("url","").replace("background-image:","").replace(" ","")
def get_dades(url):
    productes=[]
    req=requests.get(url)
    soup = BeautifulSoup(req.text,"html.parser")
    divs = soup.find_all("a",class_="search-results-row-link")

    for el in divs:
        nom = el.find(class_="search-results-row-game-title").text
        info = el.find(class_="search-results-row-game-infos").text
        preu = el.find(class_="search-results-row-price").text
        img = el.find(class_="search-results-row-image-ratio")["style"]
        productes.append({"nom":nom,"info":info,"preu":filtra_str(preu),"img":filtra_img(img)})
    return productes

def guarda_dades(productes,client=connect()):
    mydb = client.Projecte
    #Creació de la col·lecció, si ja existeix asigna aquesta a la variable mycol
    #mydb.dades.drop()
    mycol = mydb.dades
    #Si la col·lecció está buida inserta el llistat d'objectes
    if mycol.find_one()== None:
        try:
            mycol.insert_many(productes)
        except:
            
            return False
    
    return True
def mostra_dades(client=connect()):
    productes=[]
    mydb = client.Projecte
    mycol = mydb.dades
    for el in mycol.find():
        productes.append(el)
    
    return productes

def mostra_usuaris(client=connect()):
    usuaris=[]
    mydb = client.Usuaris
    mycol = mydb.dades
    for el in mycol.find():
        usuaris.append(el)
    
    return usuaris

def guarda_usuari(user,passwd,client=connect()):
    mydb = client.Projecte
    mycol = mydb.dades_usuaris
    for el in mycol.find():
        if el["user"]==user:
            
            return False

    mycol.insert_one({'user':user,'password':passwd})
    
    return True

def comprova_usuari(user,passwd,client=connect()):
    mydb = client.Projecte
    mycol = mydb.dades_usuaris
    for el in mycol.find():
        if el["user"]==user and el["password"]==passwd:
            return True
    return False

