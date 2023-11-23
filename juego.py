import random

def juego_adivinacion():
   numero_secreto = random.randint(1, 100)
   intentos = 0

   while True:
       numero_usuario = int(input("Adivina el número entre 1 y 100: "))
       intentos += 1

       if numero_usuario == numero_secreto:
           print(f"¡Felicidades! Has adivinado el número en {intentos} intentos.")
           break
       elif numero_usuario < numero_secreto:
           print("El número es mayor.")
       else:
           print("El número es menor.")

juego_adivinacion()
