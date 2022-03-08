from Caesar_Cipher import Caesar


class Password():
    def __init__(self):
        pass

    def cadastro_senha(self):
        self.password = input("Digite a sua senha: ")

        # Reverse Cipher
        # http://inventwithpython.com/hacking (BSD Licensed)

       # message = self.password
       # translated = ''
#
       # i = len(message) - 1
       # while i >= 0:
       #    translated = translated + message[i]
       #    i = i - 1
#
       # return translated

        return Caesar().encrypt(self.password)


# print(Password().cadastro_senha())
