#exercicio lista de tarefas usurio ira fazer e refazer
print('digite uma lista de tarefas')





def listar(l):
      print()
      if not l:
            print('Nao ha nenhuma tarefa')
            return
      for i in l:
            print(i,sep='\n\n')
      
def desfazer(l,a):
      print()
      if not l:
            print('Nao ha nenhuma tarefa para desfazer')
            return
      tarefa=l.pop()
      a.append(tarefa)
      
def refazer(l,a):
      print()
      if not a:
            print('Nao ha nenhuma tarefa para refazer')
            return
      tarefa=a.pop()
      l.append(tarefa)
      


      

def adicionar(lista,tarefa):
      while True:
            tarefa=input('digite uma tarefa: ')
            if tarefa== 'voltar':
                  break
            lista.append(tarefa)

      print()
      return
      
lista=[]
l_atual=[]

while True: 
        tarefa= input(' \n -Listar\n \n-Desfazer\n \n-Refazer\n \n-adicionar\n\nEscolha uma opção:')
        
        

        if tarefa == 'listar':
           listar(lista)
        
        if tarefa =='desfazer':
              desfazer(lista,l_atual)
              

        if tarefa == 'refazer':
              refazer(lista,l_atual)
            
        if tarefa == 'adicionar':
              adicionar(lista,tarefa)
