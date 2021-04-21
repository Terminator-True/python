"""
Fes un programa que llegeixi el fitxer de text "text.txt" anterior i el mostri per pantalla. Fes-lo usant les comandes open i close.

"""

try:
    f=open("text/text.txt")
    print(f.read())
    f.close

finally:
    print("Fet correctament")