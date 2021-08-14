original = input("Introduce original: ")
nueva = input(" Introduce nueva: ")


nombreFichero = "Fichero.txt"

f = open(nombreFichero,"r")

texto_original = f.read()
f.close()

texto_sustituido = texto_original.replace(original, nueva)

f = open(nombreFichero,"w")
f.write(texto_sustituido)
f.close()






    