from ejercicio5 import Usuario

class libro():
    estado = "disponible"
    apoderado = "sin apoderado"

    def __init__(self, titulo, autor, precio):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio

    def prestar(self):
        if self.estado == "disponible":
            self.estado = "prestado"
            self.apoderado = usuario1.getnombre()
            print(f"El libro '{self.titulo}' ha sido prestado con exito.")
        else:
            print(f"El libro '{self.titulo}' no está disponible por el momento")
    
    def devolucion(self):
        if self.estado == "prestado":
            self.estado = "disponible"
            self.apoderado = "sin apoderado"
            print(f"El libro '{self.titulo}' ha sido devuelto con exito.")
        else:
            print(f"El libro '{self.titulo}' no ha sido prestado, no se puede devolver.")

    def __str__(self):
        return f"{self.titulo}"
    
    def estadolibro(self):
        return f" {self.estado}"
    
    def getapoderado(self):
        return self.apoderado


class biblioteca():
    inventario =[]
    def __init__(self):
        self
    def verlibros(self):
        print("\n### LIBROS ACTUALES ###\n")
        for indice, libro in enumerate(self.inventario):
            print(f"{libro.estadolibro()} {indice+1}. {libro} PRESTADO A: {libro.getapoderado()} ")


    def agregarlibro(self, titulo, autor, precio ):
        libro1 = libro(titulo, autor, precio)
        self.inventario.append(libro1)
        print(f"libro {titulo}, del autor {autor} ha sido agregado con exito")

    def prestarlibro(self):
        seleccion= int(input("Escribe el indice del libro que quieres llevar: "))
        self.inventario[seleccion-1].prestar()
        
    
    def devolverlibro(self):
        seleccion= int(input("Escribe el indice del libro que vas a agregar: "))
        self.inventario[seleccion-1].devolucion()


    def __str__(self):
        return f"{self.inventario[0]}"
                
        

biblioteca1 =  biblioteca()
biblioteca1.agregarlibro("El Quijote", "Cervantes", 20)
biblioteca1.agregarlibro("Cien años de soledad", "Gabriel García Márquez", 25)
biblioteca1.agregarlibro("1984", "George Orwell", 15)

usuario1 = Usuario(
    input("digita tu nombre porfavor: "), input("digita tu cedula: ")
)

while True:
    print("\n####  Bienvenidos a la bibilioteca de ENCA  #### \n¿Que deseas hacer hoy? \n" \
    "\n1. Ver libros" \
    "\n2. Prestar un libro" \
    "\n3. Devolver un llibro" \
    "\n4. Salir")
    ""
    seleccion=int(input(f"Escribe el indice de tu seleccion {usuario1.getnombre()}: "))
    if seleccion == 1:
        biblioteca1.verlibros()
    if seleccion == 2:
        biblioteca1.prestarlibro()
    if seleccion == 3:
        biblioteca1.devolverlibro()
    if seleccion == 4:
        print("\n ****Esperamos verte pronto***")
        break

"""

biblioteca1.verlibros()
biblioteca1.agregarlibro("programacion", "alex", 50)
biblioteca1.verlibros()
biblioteca1.prestarlibro()
biblioteca1.prestarlibro()
biblioteca1.verlibros()
"""





