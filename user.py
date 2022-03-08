from password import Password
import json


class User():
    def __init__(self):
        pass

    def cadastro(self):
        self.nome = input("Digite o seu nome: ")
        self.email = input("Digite o seu email: ")
        self.senha = Password().cadastro_senha()

        db = {}
        db[self.email] = {}  # identificador_unico
        db[self.email]["Nome"] = self.nome
        db[self.email]["Senha"] = self.senha

        # print(db)
        with open("db.json", "w") as json_file:
            json.dump(db, json_file, ensure_ascii=False, indent=2)

        # return self.nome, self.email, self.senha
        return print("Cadastro Concluído.")
