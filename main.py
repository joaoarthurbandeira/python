from user import User
from user_specify import User_specify

profissao = input("Digite a sua profissão: ").lower()
# usuario = User()
# usuario.cadastro()
User_specify().cadastro(profissao)
