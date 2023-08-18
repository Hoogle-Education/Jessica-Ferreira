def create_conta(name, last_name, age):
  return {
    "name" : name,
    "last name": last_name,
    "age": age,
    "saldo": 0,
  }
  
def depositar(conta, valor):
  conta["endereco"] += valor

hugo = create_conta("Hugo", "Lima", 22)
hugo["nickname"] = "hgrafa"

jessica = create_conta("Jessica", "Ferreira", 23)

print(hugo["name"])