from user import User
from user_specify import User_specify

while True:  # teste para não ter que ficar digitando de novo
    profissao = input("Digite a sua profissão: ").lower()
    # usuario = User()
    # usuario.cadastro()
    # esse parametro profissao substituirá "None" no parâmetro "area" do def cadastro
    User_specify().cadastro(area=profissao)
