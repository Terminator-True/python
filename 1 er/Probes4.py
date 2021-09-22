acabat=False
while acabat!=True:
    practiques=int(input("Nota de práctiques: "))
    examen=int(input("Nota de exàmen: "))
    
    NotaFinal=int(((70*examen)/100)+((30*practiques)/100))
    if NotaFinal<=4:
        Perniler=input("La teva nota es inferior a 5... Has comprat el pernil?(S/N)")
        if Perniler=="S" or Perniler=="s":
            print("Aprovat perniler","( ❛ ͜ʖ ❛ )")
        else:
            print(":(")
    elif NotaFinal>=5:
        if NotaFinal==5:
            print("Nota mitja: ",NotaFinal," Suficient")
        elif NotaFinal==6:
            print("Nota mitja: ",NotaFinal," Bé")
        elif NotaFinal==7 or NotaFinal==8:
            print("Nota mitja: ",NotaFinal," Notable")
        elif NotaFinal==9 or NotaFinal==10:
            print("Nota mitja: ",NotaFinal," Excelent")