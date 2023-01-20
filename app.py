def calculator():
    while True:    
        ##### Define as opções de operações
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")

        ##### Insere o input para que o usuário escolha qual das operações quer fazer
        escolha = int(input(("Escolha a função: ")))

        ##### Função para realização das 4 operações, juntamente com os comandos de input dos dois números
        def numeros():
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            if escolha == 1:
                print(num1 + num2)
            elif escolha == 2:
                print(num1 - num2)
            elif escolha == 3:
                print(num1 * num2)
            elif escolha == 4:
                print(num1 / num2)
        
        #####
        if escolha == 5:
                print("Adeus!")
                break
        elif 0 > escolha < 5:
             numeros()
        
        elif escolha == 666:
             print("Não olhe para trás, ele está com você...")
             break
        
        ##### Mensagem de erro e sua interação, caso o usuário digite um número diferente das opções disponiveís 
        else:           
             print('Opção inválida, tente novamente')
             break
                  

             

calculator()
