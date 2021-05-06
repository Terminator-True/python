"""
Castiga a Python a escriure en un fitxer castiga.txt: 

1. Faré totes les tasques de python perquè vull aprovar
2. Faré totes les tasques de python perquè m’agrada programar
3. Faré totes les tasques de python perquè vull aprovar
4. Faré totes les tasques de python perquè m’agrada programar
... 
1000. Faré totes les tasques de python perquè m’agrada programar


Utilitza una funció:
escriu_castig(cadena_castig1, cadena_castig2, vegades_q_escriu) 
"""

def escriu_castig(cadena1, cadena2, voltes):
    return [cadena1 if i%2==0 else cadena2 for i in range(voltes)]

with open("text/castig.txt","w") as f:
    f.writelines(escriu_castig("Faré totes les tasques de python perquè m’agrada programar\n","Faré totes les tasques de python perquè vull aprovar\n",500))
        
