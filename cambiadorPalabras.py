import sys

if len(sys.argv) == 4:

    nombreFichero = sys.argv[1]
    original = sys.argv[2]
    nueva = sys.argv[3]

    nombreFichero = "Fichero.txt"

    f = open(nombreFichero,"r")

    texto_original = f.read()
    f.close()

    texto_sustituido = texto_original.replace(original, nueva)

    f = open(nombreFichero,"w")
    f.write(texto_sustituido)
    f.close()
        
else:
  
    print("El programa necesita 3 argumentos: Nombre Fichero, Original y Nueva")
    sys.exit(1)





    