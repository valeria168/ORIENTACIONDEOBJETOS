#El ejercicio 4 importa esta clase
class Usuario():
    def __init__ (self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula
    
    def getnombre(self):
        return self.nombre