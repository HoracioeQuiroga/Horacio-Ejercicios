#Issue numero 4 - suma - Horacio
def suma(x,y):
    return x+y

#Issue numero 7-Cociente - Horacio
def cociente(x,y):
    return float(x/y)
    
    import random
def cociente_lista(lista):
    res=[]
    for _ in lista:
        x=random.choice(lista)
        y=random.choice(lista)
        res.append(cociente([x,y]))
    return res
#Issue numero 17-Cociente Lista - Horacio 45 agregado y ejecutable  
import random
def cociente_lista (lista):
    res=[]
    for _ in lista:
        x=random.choice(lista)
        y=random.choice(lista)
        res.append(cociente([x,y]))
    return res