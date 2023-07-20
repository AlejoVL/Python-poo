class Auto:

    def __init__(self, color, marca, modelo, tipo, transmision):
        self.__llantas = 4
        self.__puertas = 4
        self.__velocidad = 0
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo
        self.transmision = transmision        
        self.freno = False
        self.encendido = False
        self.acelerar = False
        self.retroceder = False
        self.EstadoPuertas = False

    def getInfo(self):
        print("Llantas: ")
        print(self.__llantas)
        print("Puertas: ")
        print(self.__puertas)
        print("Color: " , self.color)
        print("Marca: " , self.marca)
        print("Modelo: " , self.modelo)
        print("Tipo de auto" , self.tipo)
        print("Transmision: " , self.transmision)

    def encender(self):
        print("¿QUIERES ENCENDER EL AUTO?\n\n1)Si\n2)No")
        opcion = int(input())
        
        match opcion:
            case 1:
                if (self.encendido == False):
                    self.encendido = True
                    print("Encendiendo...")
                else:
                    print("El auto ya está encendido.")
            case 2:
                print("Decidiste no encender el auto.")

    def apagar(self):
        print("¿QUIERES APAGAR EL AUTO?\n\n1)Si\n2)No")
        opcion = int(input())

        match opcion:
            case 1:
                if (self.encendido == True):
                    self.encendido = False
                    print("Apagando...")
                else:
                    print("EL auto ya está apagado.")
            case 2:
                print("Decidiste no apagar el auto.")

    def arrancar(self):
        print("¿QUIERES ARRANCAR EL AUTO?\n\n1)Si\n2)No")
        opcion = int(input())

        match opcion:
            case 1:                                
                if (self.encendido == True):
                    print("-----ACELERANDO-----")
                    for i in range(5):
                        self.__velocidad += 10                
                        print("Velocidad del auto: " , self.__velocidad , "K/h")
                else:
                    print("El auto está apagado, no es posible arrancar.")
            case 2:
                print("Decidiste no arrancar el auto.")

    def frenar(self):
        print("¿QUIERES FRENAR EL AUTO?\n\n1)Si\n2)No")
        opcion = int(input())

        match opcion:
            case 1:                            
                if(self.encendido == True and self.__velocidad > 0):
                    print("-----FRENANDO-----")
                    for i in range(5):
                        self.__velocidad -= 10
                        print("Velocidad del auto: " , self.__velocidad , "K/h")
                else:
                    print("No es posible detener el auto ya que no está en movimiento o está apagado.")
            case 2:
                print("Has decidido continuar con la marcha.")

    def reversar(self):
        print("¿QUIERES REVERSAR?\n\n1)Si\n2)No")
        opcion = int(input())

        match opcion:
            case 1:             
                if(self.retroceder == False and self.__velocidad == 0 and self.encendido == True):
                    print("-----REVERSANDO-----")
                    self.retroceder = True
                    for i in range(5):
                        self.__velocidad -= 10
                        print("Velocidad hacia atras: " , self.__velocidad, "K/h")
                        self.retroceder = False
                else:
                    print("No se puede reversar! Es posible que la velocidad del auto no sea 0 o esté apagado.")
            case 2:
                print("Decidiste no reversar.")

# auto1 = Auto("Rojo", "Mazda", 2019, "Camioneta", "4x4")
# auto1.getInfo()
# print("---------------------------------------")
# auto1.encender()
# print("---------------------------------------")
# auto1.arrancar()
# print("---------------------------------------")
# auto1.frenar()
# print("---------------------------------------")
# auto1.reversar()
# print("---------------------------------------")
# auto1.apagar()