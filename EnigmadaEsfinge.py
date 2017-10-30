import random

#Lista_Jogador = [5,6,3,2]

'''
Aqui esta sendo criado as escolhas do jogador. Nao esta sendo tratado caso o jogador tente colocar 2 numeros iguais.
obs: Na minha solução substitui as cores por numeros.
'''
Lista_Jogador = []
for i in range(4):
    Lista_Jogador.append(int(input("Digite um numero de 1 a 8: ")))

'''
Aqui esta sendo criado as escolhas do computador. Esta sendo tratado caso o computador tente dois numeros iguais.
Basicamente, se o numero nao existe na lista, ele adiciona.
'''
Lista_PC = []
i = 0
while i<4:
    x = random.randint(1,8)
    if x not in Lista_PC:
        Lista_PC.append(x)
        i = i + 1 

'''
Aqui estou imprimindo as duas listas, para fazer a conferencia visual. Evitando erros desnecessarios.
'''
#Imprime as escolhas
print(Lista_Jogador)    
print(Lista_PC)

'''
Iniciando os contadores de bolas_pretas e bolas_brancas
'''
bola_preta = 0
bola_branca = 0
'''
faz um laço de repetição variando 2 coisas ao mesmo tempo 
i = localizacao do vetor
j = Jogadas do jogador
1ª Comparacao:
    se a jogada J esta na mesma posicao da Lista de escolhas do computador. Soma-se bola_preta
    
2ª Comparacao: (Essa comparação so acontece caso a comparação anterior seja falsa)
    se a jogada J esta presente em qualquer posicao da lista de escolhas do computador. Soma-se bola_branca
'''

for i,j in enumerate(Lista_Jogador):
    print(i,j)
    if j == Lista_PC[i]:
        bola_preta += 1
    elif j in Lista_PC:
        bola_branca += 1
        
'''
Resultado
Apenas imprime na tela os resultados 
Bola Preta e Bola branca
'''
print("Resultado: ")
print(bola_preta,bola_branca)
