for i in range(2):
    print(i)


class A():
    def teste(self):
        def t1():
            print("testando")
        b = input("digite: ")
        if b == "ok":
            t1()
        return print("funcionou")

    def qualquer(self):
        self.teste()


A().qualquer()
