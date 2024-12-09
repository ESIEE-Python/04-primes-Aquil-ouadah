"""Ce code permet de vérifier si un nombre entier est premier"""
from math import sqrt

#### Fonction secondaire
    # votre code ici
def isprime(p):
    """
    Fonction qui vérifie si un nombre entier p est premier.
    """
    if p < 2:
        return False
    if p == 2:
        return True
    for d in range(2, int(sqrt(p)) + 1):
        if p % d == 0:
            return False
    return True
#### Fonction principale

def main():
    """Fonction principale qui exécute les tests"""
    # vos appels à la fonction secondaire ici
    for t in range(1, 57):  # <-- cette ligne a 5 espaces
        if isprime(t):
            print(t)
        #else:
        #    print(isprime)

    #for n in range(100):
    #    if isprime(n):
    #        print(n, end=", ")
    #print()


if __name__ == "__main__":
    main()
