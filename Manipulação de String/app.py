import os 
def exibir_nome():
      
    print ('RODIZIO DO SHARKAO\n')

def exibir_opcoes():
    print ('1. Cadastro do Cliente')
    print ('2. Menu do SHARKAO')
    print ('3. Sugestões de cardapio')
    print ('4. Sair do menu\n') 
    # Variavel armazena a opção selecionada

def finalizar_programa(): 
    os.system('cls')
    print ('Volte sempre para nadar no nosso vasto mar, shark!')

def opçoes_programa():
    opcao_selecionada = int(input('Escolha um dos numeros: ')) 
    if opcao_selecionada == 1:
         print (type(1))
         numero_escolhido = print ('Vem se tornar um shark!\nPreencha seus dados para se tornar um shark!')
         input ('Seu nome: ')
         input ('Email: ')
         input ('Telefone: ')
         print ('Parabens, agora você é um SHARK como nós')


    elif opcao_selecionada == 2:
        pass

    #Criar opção numero 2
    
    
    elif opcao_selecionada == 3:
           numero_escolhido = input ('Faça sua sugestão aqui: ')
           print ('Sua sugetão foi guardada na barriga do SHARKAO!')


    else:
        finalizar_programa()


def main ():
     exibir_nome()
     exibir_opcoes()
     opçoes_programa()



if __name__ == '__main__':
     main()


#comentario para criar segunda versão do código
     
    # Arrumar o programa que está saindo sem utilizar as outras opções
       
    # print (f'Você escolheu a opção {opcao_selecionada},','Agora escolha outra opção\n')
   


# A variavel fora do '' retorna o valor e segue o texto normalmente, 
# o str () declara o valor da variavel como string e tira o espaço que a "," coloca
