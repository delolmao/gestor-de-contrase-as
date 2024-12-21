import random as r, string as s

elements = s.ascii_letters + s.ascii_lowercase + s.ascii_uppercase + s.digits + s.punctuation
password = ""

lenght = int(input("¿De cuantos caracteres sera tu contraseña?"))
for i in range(lenght):
    print(i)
    password += r.choice(elements)
print(f"tu contraseña es: {password}")
