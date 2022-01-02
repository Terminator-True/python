"""
Fes un programa que crei un fitxer de text de nom "text.txt" i escrigui tres línies de text al fitxer. Fes-lo usant les comandes open i close. 
Comprova que s'ha creat amb un editor de text, així sabràs on els guarda.

"""

try:
    f=open("text/text.txt","w")
    lineas=["Primera línea \n","Segona línea \n","Tercera línea \n"] 
    f.writelines(lineas)
    f.close()       
finally:
    print("Fet corrctament")
