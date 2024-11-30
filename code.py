print("hello")

def table_multiplication(n):
    """Affiche la table de multiplication pour un nombre donné."""
    print(f"Table de multiplication de {n} :")
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

# Exemple d'utilisation
nombre = int(input("Entrez un nombre : "))
table_multiplication(nombre)
