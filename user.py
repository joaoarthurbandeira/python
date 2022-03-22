from password import Password
import json


class User():
    def __init__(self):
        # pass
        self.nome = input("Digite o seu nome: ")
        self.email = input("Digite o seu email: ")
        self.senha = Password().cadastro_senha()

    def cadastro(self, area=None):

        db = {}  # dados novos
        db[self.email] = {}  # identificador_unico
        db[self.email]["Nome"] = self.nome
        db[self.email]["Senha"] = self.senha
        if area != None:
            db[self.email]["Profissão"] = area
            if area == "médico":
                db[self.email]["CRM"] = input("Digite o seu CRM: ")
            elif area == "advogado":
                db[self.email]["OAB"] = input("Digite o seu OAB: ")

        # print(db)
        try:
            database = open("db.json", "r")
        # se não tiver encontrado o arquivo, interpretar o que vem abaixo:
        except FileNotFoundError:
            database = open("db.json", "w")
            database.write("{}")
            database.close()
            # database = open("db.json", "r")

        data = json.load(database)  # dados antigos

        with open("db.json", "r+", encoding="utf8") as json_file:
            data.update(db)  # dados antigos com dados novos
            json_file.seek(0)  # define a posição dos dados
            json.dump(data, json_file, ensure_ascii=False, indent=2)

        # return self.nome, self.email, self.senha
        return print("Cadastro Concluído.")
