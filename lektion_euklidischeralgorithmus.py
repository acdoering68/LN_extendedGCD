

def Teste_Ergebnis(aufgabe,ergebnis):
   match aufgabe:
       case "E1": return ergebnis==4
   return false



test4extended = [(22,5),(3,19),(24,18),(32,14),(19,2),(2,19)]

def Teste_extended_algorithm(algorithm):
    for ex in test4extended:
        g,ca,cb = algorithm(ex[0],ex[1])
        print(ex[0],ex[1],g,ca,cb,ca*ex[0]+cb*ex[1])
