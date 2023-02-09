class Velocidad:
    maximaVelocidad = "300 km"

class Cilindrada:
    cantidad =4

class Color:
    color = "Black"

class Ruedas:
    cantidad = 4

class Puertas:
    cantidad = 5


class Vehiculo:
    color = Color()
    ruedas = Ruedas()
    puertas = Puertas()


class Coche:
    velocidad = Velocidad()
    cilindrada = Cilindrada()
    vehiculo = Vehiculo()


c = Coche()
print("El color de este Coche es: ", c.vehiculo.color.color)
print("La Velocidad es de: ", c.velocidad.maximaVelocidad)
print("La cantidad de puertas son: ", c.vehiculo.puertas.cantidad)
print("La cantidad de puertas son: ", c.vehiculo.ruedas.cantidad)





