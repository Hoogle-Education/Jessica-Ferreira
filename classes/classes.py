
      
class Circulo:
  PI = 3.14159265 # atributo estatico
  
  def __init__(self, raio):
    self.raio = raio
    
  @property # decorator - marca como algo
  def area(self):
    return (self.raio**2) * Circulo.PI
  
  @property
  def perimetro(self):
    return 2* self.raio * Circulo.PI
  
  def calcula_area(raio):
    return (raio**2) * Circulo.PI
    
# fruto do molde

joao = Conta("Joao da Silva") 
# joao.nome = "Joao da Silva"
# joao.saldo = 0

maria = Conta("Maria da Silva")
# maria.nome = "Maria da Silva"

circulo = Circulo(4)

# print(circulo.area()) #sem decorator
print(f'Area = {circulo.area}')
print(type(Circulo.calcula_area(5)), Circulo.calcula_area(5))

lista = [1, 2, 3]
len(lista) # lista.length

joao.nome = "Joao Pedro"

print(joao.nome)

joao.depositar(200)
joao.sacar(100)

print(joao.saldo)

print(maria.nome)