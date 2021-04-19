x = 10
y = 10
def creaTauler(x,y):
    m=[]
    for i in range(x):
        fila=[]
        for j in range(y):
                fila.append([False,"~"])
        m.append(fila)
    return m

ll=[[[False,"~"] for j in range(y)]  for i in range(x)]

if ll==creaTauler(x,y):
    print("Si")
