# ======================================================================
# 🚀 Desafio Extra: Sistema de Login Simples
# ======================================================================


# Usamos um dicionário onde a CHAVE é o nome do usuário

usuarios = {
    "admin": "admin123",
    "joao": "senha123",
    "maria": "abc456"
}

# ======================================================================

# A função 'validar_login' recebe o nome e a senha digitados.
def validar_login(nome_usuario, senha_digitada):
    # Verificamos se o nome de usuário existe no nosso dicionário.
    if nome_usuario in usuarios:
     
        if usuarios[nome_usuario] == senha_digitada:
            return True  # Login bem-sucedido!
        else:
            return False # Senha incorreta.
    else:
        return False # Usuário não encontrado.

# ======================================================================

# O loop pede o login até que a validação seja verdadeira.
while True:
    print("\n--- Sistema de Login ---")
    nome_usuario = input("Digite seu nome de usuário (ou 'sair' para fechar): ")
    
   
    if nome_usuario.lower() == 'sair':
        print("👋 Fechando o programa. Até mais!")
        break
    
    senha_digitada = input("Digite sua senha: ")

    
    if validar_login(nome_usuario, senha_digitada):
        print(f"\n🎉 Login bem-sucedido! Bem-vindo(a), {nome_usuario}!")
        break # O login deu certo, então saímos do loop.
    else:
        print("\n❌ Login inválido. Tente novamente.")

# ======================================================================
# 🏁 Fim do Programa
# ======================================================================
