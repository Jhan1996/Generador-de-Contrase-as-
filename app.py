import random
import string

# Se define una funcion que contendra 3 variables
def generate_password():
   # Esta variable guarda un numero aleatorio entre 8 y 32
    length = random.randint(8, 32)
    characters = string.ascii_letters + string.digits + string.punctuation
  # Esta variable utiliza un for loop que itera sobre la variable length para definir la longitud de la contrasena
    password = ''.join(random.choice(characters) for i in range(length))
    return password

print(generate_password()) 
