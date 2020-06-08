from string import ascii_letters, digits
from itertools import product
from time import time

caracteres = ascii_letters + digits

def buscar(con):
    archivo = open("combinaciones.txt","w")
    if 3<= len(con) <=4:
        for i in range(3,5):
            for comb in product(caracteres, repeat=i):
                prueba = "".join(comb)
                archivo.write(prueba+"\n")
                if prueba == con:
                    print("La contraseña es:  ", format(prueba))
                    archivo.close()
                    break
    else:
        print("Ingresa una contraseña de 3 a 4 caracteres.\n")

if __name__ == "__main__":
    con=input("Ingresa la contrasena:\n")
    t0 = time()
    buscar(con)
    print("Tiempo de ejecucion: ", format(round(time()-t0,6)))


#Fuerza bruta