#este programa abre y lee un texto y verifica si alguna palabra
#esta en una lista almacenada en la web
#retorna true si coincide alguna palabra

import urllib.request
def leer_text():
    frases = open("/Users/JL/Documents/python/udacity/frases_plain.txt")
    miTexto = frases.read()
    print (miTexto)
    frases.close()
    chequea_palabra(miTexto)

def chequea_palabra(chequear):
    # aqui se pone la palabra a chequear
    listaChequeo = urllib.request.urlopen("http://www.wdylike.appspot.com/?"+urllib.parse.urlencode([('q',chequear)]))
    salida = listaChequeo.read()
    print (salida)
    listaChequeo.close()

leer_text()
