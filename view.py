from model import Login, base, session
from dal import LoginDal
from controller import LoginController


class loginView:
    @classmethod
    def menu(cls):
        n1 = input("Escolha uma opção\n1-Cadastrar\n2-Login\n")
        return n1

    @classmethod
    def options(cls):
        answer = loginView.menu()
        if answer == "1":
            name = input("Digite o seu nome\n")
            email = input("Digite ao e-mail\n")
            passw = input("Digite a senha\n")
            try:
                LoginController.register(name, email, passw)
            except:
                print("Erro ao cadastrar\n")
        elif answer == "2":
            email = input("Digite ao e-mail\n")
            passw = input("Digite a senha\n")
            try:
                LoginController.logar(email, passw)
            except:
                print("Erro ao cadastrar\n")
        else:
            print("Digite dados validos\n")
            loginView.menu()


loginView.options()
