# função para numero primo

def encontra_primo(n):
    lista_nao_primo=[]
    lista_primo=[]
    for i in n:
        if i < 2:
            print(f'{i} nao é um numero primo')
        # a Ideia e j iniciando em dois ira percorrer ate a raiz quadrada de i +1
        # usando o i**0.5 para percorrer ate a raiz quadrada  diminindo o tamanho do codigo
        for j in range(2,int(i**0.5,)+1):
            if i%j==0:
                lista_nao_primo.append(i)
                
        if i>= 2:   
            if i not in lista_nao_primo:
                lista_primo.append(i)
    print(lista_primo)
    return lista_nao_primo

lista=[1,10,30,11,3,9]
encontra_primo(lista)