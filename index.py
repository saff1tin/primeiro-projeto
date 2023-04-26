import random

chute = int(input('Insira um número entre 1 e 100: \n'))
#print(chute)
numero_secreto = random.randint(1, 100)
#print(numero_secreto)

#verifica e declara caso o valor recebido seja inválido
if chute <= 0 or chute > 100:
  print('Número inválido.')

#começa o loop qnd o valor recebido é válido
while chute > 0 and chute < 101:    
  
  #verifica primeiro se o valor recebido confere com o número aleatório gerado
  if chute == numero_secreto:
    #caso sim, retorna ao usuário uma mensagem de vitória junto ao número
    print(f'Parabéns, você adivinhou! O número secreto era {numero_secreto}')
 
  else:
    #inicia outro loop para que seja possível a verificação enquanto o numero
    #recebido for diferente do número da máquina
    while chute != numero_secreto:
      if chute > numero_secreto:
        print('Menos!')
        chute = int(input('Insira um número entre 1 e 100: \n'))

        if chute == numero_secreto:
          print(f'Parabéns, você adivinhou! O número secreto era {numero_secreto}')

      elif chute < numero_secreto:
        print('Mais!')
        chute = int(input('Insira um número entre 1 e 100: \n'))

        if chute == numero_secreto:
          print(f'Parabéns, você adivinhou! O número secreto era {numero_secreto}')
        
  break
