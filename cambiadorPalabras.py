import sys

argumentos = sys.argv

nombreFichero = argumentos[1]
original = argumentos[2]
nueva = argumentos[3]

nombreFichero = "Fichero.txt"

f = open(nombreFichero,"r")

texto_original = f.read()
f.close()

texto_sustituido = texto_original.replace(original, nueva)

f = open(nombreFichero,"w")
f.write(texto_sustituido)
f.close()






    