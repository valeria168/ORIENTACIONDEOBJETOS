class computadora:
    def __init__(self, marca, procesador, RAM, tarjeta_video, disco_duro):
        self.marca = marca
        self.procesador = procesador
        self.ram = RAM
        self.tarjeta_video = tarjeta_video
        self.disco_duro = disco_duro

    def mostrar_informacion(self):
        print("La computadora tiene la siguiente información:")
        print(f"Marca: {self.marca}")
        print(f"Procesador: {self.procesador}")
        print(f"RAM: {self.ram} GB")
        print(f"Tarjeta de video: {self.tarjeta_video}")
        print(f"Disco duro: {self.disco_duro} GB")
#Crear objeto  
Mi_pc = computadora("DELL", "Core icore 7", "8", "NVIDIA GeForce RTX 3060", "512 GB SSD")
#llamar info
Mi_pc.mostrar_informacion()     