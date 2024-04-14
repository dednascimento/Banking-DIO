
# SISTEMA DE BANKING - DEIVID BANK

def armazenarDados(usuarios, nome, data_nacimento, cpf, endereco, tipo_contrato, senha_usuario):
    pass

def validacao_senha():
    pass

def validacao_endereo():
    pass

def validacao_cpf():
    pass

def cadastrar():
    nome = str(input("\nPrimeito digite seu nome completo. \nNome:")).strip().title()
    data_nascimento = str(input("\nDigite sua data de nacimento (Dia/Mês/Ano) \nData de Nacimento:"))
    cpf = int(input('\nDigite seu CPF (Sem pontuação, apenas números) \nR:'))
    endereco = str(input('Digite seu endereço completo (Logradouro, Numero, Bairro - Cidade/Sigla)'))
    tipo_contrato = str(input('Seu contrato é CORPORATIVO OU PESSOAL ? R:'))
    senha_usuario = str(input('Digite sua senha: '))

def loginUsuario(nome, cpf, senha_usuario):
    pass
    
incio = """

====================================
-     DEIVID BANKING (ONLINE)      -
====================================
-                                  
-     SEJA MUITO BEM-VINDO !!      
-                                  
-     1 - FAÇA JÁ SEU CADASTRO!                 
-     2 - JÁ SOU USUÁRIO                 
-                                  
====================================

Nome Completo:"""

optionUser = """
====================================
-     DEIVID BANKING (ONLINE)      -
====================================
-                                  
-     O que você precisa  ??       
-                                  
-     1 -> SAQUE                   
-     2 -> DEPÓSITO               
-     3 -> EXTRATO                 
-     4 -> SAIR                   
-                                  
====================================

R: """

def confirmacoes_user():
    optionInicial = input(incio)
    if optionInicial == '1':
        cadastrar()

# OPÇÕES DE EXTRATO
def printExtrato(extrato):
    
    if len(extrato) == 0:
        "Não foram realizadas movimentações." 
    else:
        for movimentacao in extrato:
            global extrato_final 
            extrato_final = extrato_final + "" + f"-     {movimentacao}"
          
# VALIDAÇÃO DE SAC
def validar_saque(*, valor, saldo, limite, numero_de_saques, limite_para_saques):
    # VALOR MAIOR QUE O SAQUE
    if valor > saldo:
        print(f"\nVocê não possui saldo suficiente. \nValor do saque: R$ {valor}\nSaldo Atual: R$ {saldo}\n")
        return False
        
    # VALOR MAIOR QUE O LIMITE
    elif valor > limite:
        print(f"\nO valor indicado para saque ultrapassou o limite. \nValor limite: R$ {limite} \nValor do saque: R$ {valor}\nSaldo Atual: R$ {saldo}\n")
        return False
    
    # VALOR MAIOR/IGUAL A LIMITES DE SAQUES
    elif numero_de_saques >= limite_para_saques:
        quantidade_excedida = print(f"\nVocê excedeu a quantidade máxima de saques. \Limite de saques: R$ {limite_para_saques} \nValor do saque: R$ {valor}\nSaldo Atual: R$ {saldo}\n")
        return False
    
    # SAQUE APROVADO
    elif valor > 0:
        print('\nProcessando...')
        return True
    
    else:
        print("\nO valor informado é inválido.")  
 
# SAQUE E DEPÓSITO  
def saque(*, saldo, valor, extrato, numero_de_saques):
    print(f"\nSaldo anterior: R$ {saldo:.2f}")
    saldo -= valor
    numero_de_saques += 1
    extrato.append(f"\nSaque: R$ {valor:.2f}\n")
    return saldo, extrato
def deposito(saldo, valor, extrato):
    saldo += valor
    extrato.append(f"Depósito: R$ {valor}\n")
    return saldo, extrato

# MENU DO USUÁRIO    
def menu_opcoes():
    saldo_atual = 0
    valor_limite = 500
    saques_usados = 0
    limite_de_saque = 3
    extrato = []
    
    while True:
        opcao = input(optionUser)
        if opcao == "1":
            valor_saque = float(input("Informe o valor do saque: R$"))        
            validacao = validar_saque(saldo=saldo_atual, valor=valor_saque, limite=valor_limite, numero_de_saques=saques_usados, limite_para_saques=limite_de_saque)

            if validacao == True:
                saldo_atual, extrato = saque(saldo=saldo_atual, valor=valor_saque, extrato=extrato, numero_de_saques=saques_usados)
                print(f"Valor do saque: R$ {valor_saque}\n -> Saldo Atual: R$ {saldo_atual}\n")
            else:
                print("Tente novamente.")
        elif opcao == "2":
            valor = float(input("Informe o valor do depósito: "))
            if valor > 0:
                saldo_atual, extrato = deposito(saldo_atual, valor, extrato)
                print(f"Depósito: R$ {valor}\nSaldo Atual: R$ {saldo_atual}\n")
            else:
                print("Operação falhou! O valor informado é inválido.") 
        elif opcao == "3":  
            printExtrato(extrato)     
            print(
f"""
====================================
-     DEIVID BANKING (ONLINE)      -
====================================
-                                  
-     Saldo: R$ {saldo_atual:.2f}   
-     
-     SUAS MOVIMENTAÇÕES:
-     \n{extrato_final}-
-
-                                  
====================================
""")    
            extrato_fim = "" # FAZENDO RESET PARA NÃO DUPLICAR VALORES
        elif opcao == "4":
            break
        else:    
            print("Operação inválida, por favor selecione novamente a operação desejada.")

# ESTRTUTURA PRINCIPAL
def main():   
       
    # PARA CADASTRAR - NOVOS USUÁRIOS
    conta = ''
    nome = ''
    data_nascimento = ''
    cpf = ''
    endereco = ''
    tipo_contrato = ''
    senha_usuario = ''

    # LISTA DE USUÁRIOS
    lista_usuarios = {
        "usuarios_cadastrados": {
            conta: [],
            cpf: [],
            nome: [],
            data_nascimento: [],
            tipo_contrato: [],
            endereco: [],
            senha_usuario: []
        }
    }
    
    confirmacoes_user()
    
    extrato_final = '' 
    menu_opcoes()
main()         

            