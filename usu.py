"""Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, 
mostrando uma mensagem de erro e voltando a pedir as informações."""

user = input("Nome de usuário: ")
senha = input("Senha: ")
while user == senha:
    print('Erro! Os campos usuário e senha não podem ter o mesmo valor.')
    user = input("Nome de usuário: ")
    senha = input("Senha:")
else: print('Cadastro efetuado com sucesso!')