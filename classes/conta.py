# molde - tipo personalizado
class Conta: 
  # (metodo) construtor
  def __init__(self, nome, apelido=""):
    print("construtor chamado")
    self._nome = nome
    self.apelido = apelido if apelido != "" else nome
    self._saldo = 0
    
  @property # getter
  def saldo(self):
    return self._saldo
    
  @property
  def nome(self):
    return self._nome
  
  @nome.setter
  def nome(self, nome):
    self._nome = nome
    
  # comportamentos - metodos - faz
  def depositar(self, quantia):
    self._saldo += quantia
    
  def sacar(self, quantia):
    if self._saldo >= quantia:
      self._saldo -= quantia