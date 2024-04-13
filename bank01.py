
# SISTEMA DE BANKING - DEIVID BANK

dados = {
    "saldo": 0,
    "valor_limite": 500,
    "saques_atual": 0,
    "limite_saque": 3   
}

extrato = []

incio = """

====================================
-     DEIVID BANKING (ONLINE)      -
====================================
-                                  -
-     SEJA MUITO BEM-VINDO !!      -
-                                  -
====================================

"""

menu = """

====================================
-     DEIVID BANKING (ONLINE)      -
====================================
-                                  
-     O que você precisa  ??       
-                                  
-     1 -> DEPÓSITO                   
-     2 -> SAQUE                
-     3 -> EXTRATO                 
-     4 -> SAIR                   
-                                  
====================================

R: """

extrato_fim = '' 
  
def printExtrato():
    if len(extrato) == 0:
        "Não foram realizadas movimentações." 
    else:
        for movimentacao in extrato:
            global extrato_fim 
            extrato_fim = extrato_fim + "" + f"-     {movimentacao}"
            
    

while True:
    
    opcao = input(menu)
    print(opcao)
    # PROCESSOS DE DEPÓSITO
    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            dados["saldo"] = dados["saldo"] + valor
            extrato.append(f"Depósito: R$ {valor}\n")
            print(f"Depósito: R$ {valor}\nSaldo Atual: R$ {dados['saldo']}\n")
        else:
            print("Operação falhou! O valor informado é inválido.")
         
    # ME SEGURANDO PARA NÃO USAR FUNÇÕES :V

    # PROCESSO PARA SACAR   
    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > dados["saldo"]
        # VALOR MAIOR QUE O SAQUE
        excedeu_limite = valor > dados["valor_limite"]
        # VALOR MAIOR QUE O LIMITE
        excedeu_saques = dados["saques_atual"] >= dados["limite_saque"]
        # VALOR MAIOR/IGUAL A LIMITES DE SAQUES
        
        if excedeu_saldo:
            print("Você não possui saldo suficiente.")

        elif excedeu_limite:
            print("O valor indicado para saque ultrapassou o limite.")

        elif excedeu_saques:
            print("Você excedeu a quantidade máxima de saques.")

        elif valor > 0:
            dados["saldo"] = dados["saldo"] - valor
            extrato.append(f"Saque: R$ {valor:.2f}\n")
            dados["saques_atual"] += 1
            print(f"Valor do saque: R$ {valor}\nSaldo Atual: R$ {dados['saldo']}\n")

        else:
            print("O valor informado é inválido.")

    elif opcao == "3":  
        printExtrato()     
        print(
f"""
====================================
-     DEIVID BANKING (ONLINE)      -
====================================
-                                  
-     Saldo: R$ {dados['saldo']:.2f}   
-     
-     SUAS MOVIMENTAÇÕES:
-     \n{extrato_fim}-
-
-                                  
====================================
""")    
        extrato_fim = "" # FAZENDO RESET PARA NÃO DUPLICAR VALORES

    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        

        