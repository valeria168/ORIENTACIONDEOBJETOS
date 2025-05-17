class computer:
    def __init__(self, marca, modelo, sistema_operativo, encendida = False, saludo=False):
       self.marca = marca
       self.modelo = modelo 
       self.sistema_operativo = sistema_operativo
       self.encendida = encendida
       self.saludo = saludo
           
    def encender(self):
        self.encendida = True
        print(f"{self.marca} {self.modelo} encendido el equipo.")
        self.saludar()
    
    def saludar(self):
        print(f"iniciando sesion {self.marca} {self.modelo} hola Enca24 Bienvenido.")
       
    def apagar(self):
       if self.encendida:
          self.encendida = False
          print(f"{self.marca} {self.modelo} se ha apagado el equipo.")
       else:
          print(f"{self.marca} {self.modelo} se apago el equipo.")
        
    def actualizar(self, nuevo_sistema_operativo):
       if self.encendida:
          print(f"actualizando {self.marca} {self.modelo} de {self.sistema_operativo} a {nuevo_sistema_operativo}...")
          self.sistema_operativo = nuevo_sistema_operativo
          print("actualizacion finalizada.")
       else:
          print(f"no se puede actualizar{self.marca} {self.modelo} por que esta apagado.")
      
    def estado(self):
       estado = "encendida" if self.encendida else "apagada"
       print(f"{self.marca} {self.modelo} esta actualmente {estado} con {self.sistema_operativo}.")
    
         
# ejemplo de uso
pc1 = computer("hp", "desktop", "windows 11 pro")
pc1.estado()
pc1.encender()
pc1.actualizar("windows 11")
pc1.estado()
pc1.apagar()
pc1.estado()