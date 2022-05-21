class Cuenta:
    def __init__(self,titular="Estefania", cantidad=8000):
      self.titular=titular
      self.cantidad=cantidad

    def mostrar(self):
      print(f"{self.titular} tiene en su cuenta {self.cantidad}")
    def  ingresar(self,cantidad):
      self.cantidad +=cantidad
      print("Acabo de ingresar {4000}")
    def retirar(self,cantidad):
      self.cantidad -=cantidad
      print("Acabo de retirar {2000}")

cuenta=Cuenta("Estefania", 8000)
cuenta.mostrar()
cuenta.ingresar(4000)
cuenta.retirar(2000)