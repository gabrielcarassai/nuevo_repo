class Carro():
    color = "Azul"
    marca = "Audi"
    combustible = "Gasolina"
    tipo = "Sedan"
    puertas = 4
    luces = "LED"

    def encendido(self):
        print(f'mi carro es un {self.marca} color {self.color} tiene un motor a {self.combustible}')

a = Carro.encendido
a.encendido()