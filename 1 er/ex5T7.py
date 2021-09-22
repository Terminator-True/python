"""
Fes un programa en Python anomenat ex5.py que accepta una data com a argument, 
en format dd/mm/aaaa, comprova que el format és correcte i ens retorna a quin dia de 
la setmana correspon. Podeu fer servir la biblioteca datetime.
"""
import datetime,sys

def dataValida(data):

  try :
        dia,mes,año = data.split('/')
        isValidDate = True
        datetime.datetime(int(año),int(mes),int(dia))
  except ValueError :
       isValidDate = False

  if(isValidDate) :
      print ("El format es correcte (DD/MM/YYY) : "+User_input)
  else :
      print ("El format no es el correcte (DD/MM/YYY) : " +User_input)
User_input=sys.argv[1]
dataValida(User_input)
