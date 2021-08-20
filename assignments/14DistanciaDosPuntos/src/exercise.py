import math
def main():
    #escribe tu código abajo de esta línea
    a = int(input("x1= "))
    b = int(input("y1= "))
    c = int(input("x2= "))
    d = int(input("y2= "))
   

    distancia = math.sqrt((c-a)**2+(d-b)**2)
    redondeado = round(distancia, 2)

    print ("distancia= "+str(redondeado))


if __name__ == '__main__':
    main()
