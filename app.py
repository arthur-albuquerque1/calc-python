def calculator():
    while True:    
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")

        escolha = int(input(("Escolha a função: ")))

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

        if escolha == 5:
                print("Adeus!")
                break
        elif 0 > escolha < 5:
             numeros()
        else:
             erro_escolha = int(input(("Esta opção é inválida, escolha novamente digitando 1, ou feche o programa digitando 2: ")))
             if erro_escolha == 1:
                  calculator()
             elif erro_escolha == 2:
                  print("Adeus!")
                  break

             

calculator()