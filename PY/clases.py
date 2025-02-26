class mascota:
    nombre = ""
    especie = ""
    raza = ""
    edad = 0
    
    def __init__(self,nombre,especie="gato",raza="persa",edad=10):
        """"constructor de la clase mascota"""
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.edad = edad
    
    def habla(self):
        """funcion de mensaje"""
        print(f"hola, soy {self.nombre} de la especie {self.especie}")
        print(f"de raza {self.raza} y edad {self.edad} años")
        if self.especie.lower() == "perro":
            print(f"guauuu")
        elif self.especie.lower() == "gato":
            print(f"miauuuuuuuuuuuuuuu")
        else:
            print(f"hago no se como")
            
m1 = mascota("morita")
m1.habla()
m2 = mascota("michi","gato","siames",20)
m2.habla()
m3 = mascota("tony","perro")
m3.habla()
m4 = mascota("tony","roedor")
m4.habla()