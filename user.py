from password import Password
import json
from envia_email import send_email
import random
import string


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

        try:
            database = open("db.json", "r")
        # se não tiver encontrado o arquivo, interpretar o que vem abaixo:
        except FileNotFoundError:
            database = open("db.json", "w")
            database.write("{}")
            database.close()
            # database = open("db.json", "r")

        data = json.load(database)  # dados antigos

        def armazena():
            if area != None:
                db[self.email]["Profissão"] = area
                if area == "médico":
                    db[self.email]["CRM"] = input("Digite o seu CRM: ")
                elif area == "advogado":
                    db[self.email]["OAB"] = input("Digite o seu OAB: ")

            # print(db)
                with open("db.json", "r+", encoding="utf8") as json_file:
                    # dados antigos com dados novos (db, que ta num dicionario)
                    data.update(db)
                    json_file.seek(0)  # define a posição dos dados
                    # empurrar os dados pro nosso json, quem atualiza de fato o arquivo
                    json.dump(data, json_file, ensure_ascii=False, indent=2)

        if self.email in data:
            print("Dados já existentes. Deseja atualizá-los? [S/n]")
            atualiza = input().lower()
            if atualiza == "s":
                # variavel nova para armazenar um dado antigo (senha antiga)
                # o que está no db
                senha_cadastrada_db = data[self.email]["Senha"]
                # se a senha atual (self.senha) for igual à antiga...
                if self.senha == senha_cadastrada_db:
                    armazena()
                else:
                    # nesse momento, restam 2 tentativas (primeira realizada ao digitarmos: " self.senha = Password().cadastro_senha()" "" que é comparada em "if self.senha == senha_cadastrada_db:"" )
                    for num_tentativa in range(2):
                        if num_tentativa < 2:
                            print(
                                f"senha incorreta!\nDados já existentes. Deseja atualizá-los? [S/n]\nRestam {2 - num_tentativa} tentativas.")
                            atualiza = input().lower()
                            if atualiza == "s":
                                self.senha = input("digite a senha novamente ")
                                if self.senha == senha_cadastrada_db:
                                    armazena()  # se ela acertar...
                                    break
                            else:  # se ela não quiser atualizar
                                break
#
                        # se ela errar e não tiver excedido, volta para começo do for loop.
                        if num_tentativa == 1:
                            # se ela errar e exceder o numero de tentativas
                            self.codigo = random.choices(
                                string.ascii_letters + string.digits, k=6)
                            send_email(self.email, self.codigo, self.nome)
                            # print(
                            #     "enviamos um código para redefinição de senha no seu email.")

        # if self.email in data:
            # print("Dados já existentes. Deseja atualizá-los? [S/n]")
            # atualiza = input().lower()
            # if atualiza == "s":
                # for num_tentativa in range(3):
                    # if num_tentativa < 3:
                        # senha_cadastrada_db = data[self.email]["Senha"]
                        # if self.senha == senha_cadastrada_db:
                            # armazena()
                            # break
                        # else:
                            # print(
                            # f"senha incorreta!\nDados já existentes. Deseja atualizá-los? [S/n]\nRestam {3 - num_tentativa} tentativas.")
                            # atualiza = input().lower()
                            # if atualiza == "s":
                            #     if self.senha == senha_cadastrada_db:
                            #         armazena()
                            #     break
                            # else:
                            #     break
#
                # if num_tentativa == 3:
                    # print(
                        # "enviamos um código para redefinição de senha no seu email.")

                        #
#
        return self.nome, self.email, self.senha
        return print("Cadastro Concluído.")
