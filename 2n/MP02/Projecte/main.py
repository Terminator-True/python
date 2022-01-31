from urllib import request
import requests
from bs4 import BeautifulSoup
import pandas as pd

def filtra_str(string):
    return string.replace(" ","").replace("\n","")
def get_dades(url):
    productes=[]
    req=requests.get(url)
    soup = BeautifulSoup(req.text,"html.parser")
    divs = soup.find_all("a",class_="search-results-row-link")

    for el in divs:
        nom = el.find(class_="search-results-row-game-title").text
        info = el.find(class_="search-results-row-game-infos").text
        preu = el.find(class_="search-results-row-price").text
        productes.append((nom,info,filtra_str(preu)))
    print(productes)

if __name__=="__main__":
    get_dades("https://www.allkeyshop.com/blog/catalogue/category-pc-games-all/")
