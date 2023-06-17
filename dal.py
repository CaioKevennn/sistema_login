from model import  Login, base, session
from hashlib import sha256
#Tem alguma coisa que não seguea pep 8? Se sim, o que?
class LoginDal(base):
    __tablename__='login'
    @classmethod
    def register(cls,user:Login):
        user.passw=sha256(user.passw.encode())
        session.add(user)
        session.commit()
    @classmethod
    def login(cls,email,passw):
        x=session.query(Login).filter(Login.email==email).one()
        if x.passw==sha256(passw.encode()):
            return("Login realizado com sucesso")
        else:
            return("Verifique sua senha")






