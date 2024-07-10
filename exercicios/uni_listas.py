# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

mini_valor= min(len(l1)),min(len(l2))

new_lista=[(l1[i],l2[i]) for i in range(mini_valor)]

                
        

    
l1=['Salvador', 'Ubatuba', 'Belo Horizonte']
l2=['BA', 'SP', 'MG', 'RJ']
zipper(l1,l2)
