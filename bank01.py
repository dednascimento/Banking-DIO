
# SISTEMA DE BANKING - DEIVID BANK

init_message = """

====================================
-     DEIVID BANKING (ONLINE)      -
====================================
-                                  -
-     SEJA MUITO BEM-VINDO !!      -
-                                  -
====================================

"""

username = ""
cpf_user = ""
pin_user = ""

dadosCliente = {
    "Username": username,
    "CPF": pin_user,
    "Senha": cpf_user,
    "SAQUE": [],
    "DEPÓSITO": []
}

signin_message = f"""

======================================
-     DEIVID BANKING (ONLINE)        -
======================================
-                                    
-       ! Realize seu login:           
-                                    
-       -> NOME  [{username}]           
-       -> CPF   [{cpf_user}]           
-       -> PIN   [{pin_user}]           
-                                    
======================================
 
"""

welcome_message = f"""

====================================
-     DEIVID BANKING (ONLINE)      -
====================================
-                                  
-     SEJA MUITO BEM-VINDO !!      
-     -> {username}      
-                                  
====================================

"""

option_message = """

====================================
-     DEIVID BANKING (ONLINE)      -
====================================
-                                  -
-     O que você precisa  ??       -
-                                  -
-     1 -> SAQUE                   -
-     2 -> DEPÓSITO                -
-     3 -> EXTRATO                 -
-     4 -> SAIR                    -
-                                  -
====================================

R: 
"""

def menu_iniciar():
    print(init_message)

    i = 0
    while i <= 3:

        global username, cpf_user, pin_user

        # PEDINDO NOME
        username = input(signin_message + "\nDigite seu nome: ").strip()
        i += 1

        # PEDINDO CPF
        cpf_user = input(signin_message + "\nDigite seu CPF: ").strip()
        i += 1

        pin_user = input(signin_message + "\nDigite sua senha: ").strip()
        i += 1

        return signin_message



menu_iniciar()


# -> USUÁRIO
# SAQUE, EXTRATO E DEPÓSITO













# ------
# DEPÓSITO:
# VALORES POSITIVOS.
# ARMAZENAR EM 'BD'

# ------
# SAQUE:
# 3 SAQUES
# VALORES DE ATÉ 500,0 (CDA)
# ARMAZENAR EM 'BD'


# ------
# EXTRATO:
# INFORMAÇÕES = 'BD'
# FORMATAÇÃO MONETÁRIA `R$ XXXX.XX`
