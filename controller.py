from model import Login, base, session
from dal import LoginDal


class LoginController(base):
    __tablename__ = "login"

    @classmethod
    def email_exist(cls, email):
        x = session.query(Login).all()
        for i in x:
            if i.email == email:
                return True
        return False

    @classmethod
    def register(cls, name, email, passw):
        if name.strip() == "" or len(name.strip()) > 50:
            print("Digite um nome valido")
        if "@" not in email or email.strip() == "":
            print("Digite um e-mail valido")
        if len(passw) > 6:
            if LoginController.email_exist(email) == False:
                try:
                    LoginDal.register(Login(name=name, email=email, passw=passw))
                    print("Registro realizado com sucesso")
                except Exception as e:
                    print(f"Erro{e} ao tentar registrar")
            else:
                print("E-mail já cadastrado")
        else:
            print("Digite uma senha valida")

    @classmethod
    def logar(cls, email, passw):
        if LoginController.email_exist(email) == True:
            try:
                LoginDal.login(email, passw)
                print("Login Realizado com sucesso")
            except Exception as e:
                print(f"Falha ao registrar e-mail. Erro:{e}")
        else:
            print("E-mail não cadastrado")


LoginController.logar("´3caiokevpe@gmail.com", "1234567")
