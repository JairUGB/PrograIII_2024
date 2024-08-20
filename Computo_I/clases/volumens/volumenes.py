import math

def volumen_cilindro(radio, altura):
    
    return math.pi * radio**2 * altura

def volumen_cono(radio, altura):
    
    return (1/3) * math.pi * radio**2 * altura

def volumen_esfera(radio):
   
    return (4/3) * math.pi * radio**3

if __name__ == "__main__":

    radio_cilindro = 5
    altura_cilindro = 10
    print(f"Volumen del cilindro: {volumen_cilindro(radio_cilindro, altura_cilindro)}")

    radio_cono = 5
    altura_cono = 10
    print(f"Volumen del cono: {volumen_cono(radio_cono, altura_cono)}")

    radio_esfera = 5
    print(f"Volumen de la esfera: {volumen_esfera(radio_esfera)}")