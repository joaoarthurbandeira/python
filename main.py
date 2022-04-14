from user import User
from user_specify import User_specify

while True:  # teste para não ter que ficar digitando de novo
    profissao = input("Digite a sua profissão: ").lower()
    # usuario = User()
    # usuario.cadastro()
    # esse parametro "area" receberá como argumento "profissao", que substituirá "None" no parâmetro "area" do def cadastro
    User().cadastro(area=profissao)
