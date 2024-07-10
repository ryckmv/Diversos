

lista=[]

for i in range(0,5):
    n = int(input('digite: '))
    if n >= 0 :
        
   
        pos=0
        while pos < len(lista) and n> lista[pos]:
           pos+=1
        lista.insert(pos,n)

    
print(lista)