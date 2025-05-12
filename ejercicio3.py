#clase estudiante con metodo con metodo para calcular promedio

class estudiante:
    materias={}
    def __init__ (self):
        self.materias

    def agregarmateria(self):
        self.materias[input("Escriba la materia que quiere agregar: ")]=0 
    def setnotas(self):
        for indice, materia in enumerate(self.materias):
            self.materias[materia]=float(input(f"dijite la nota de {materia}: "))
    
    def calcularpromedio(self):
        promedio = 0
        suma = 0
        for indice, materia in enumerate(self.materias):
            suma += self.materias[materia]
        return f"El promedio es: {suma/len(self.materias)} "
        


estudiante1= estudiante()
estudiante1.agregarmateria()
estudiante1.agregarmateria()
estudiante1.setnotas()


print(estudiante1.calcularpromedio())
