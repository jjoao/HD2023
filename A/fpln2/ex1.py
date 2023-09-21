# Ex0
#   print("voS")

# Ex1 Dado um texto
#   calcular o seu comprimento (nº de caracteres do texto)
#   Quantas linhas
#   Quantas palavras
#   e já agora... quantas frases
# ... texto lido a partir de um ficheiro

texto2 = """SUBLime (Sustainable Building Lime Applications via Circular Economy 
                   and Biomimetic Approaches) aims to train researchers in multiple 
scientific and engineering fields for a better understanding and development of 
sustainable innovation solutions for mortars, renders and plasters in new construction
 and conservation of the built heritage. This conference will be a key platform for 
dissemination of the SUBLime’s results, and everyone is invited to participate. This is 
also a great opportunity to discuss and share on-going research on sustainable masonry systems 
and! other challenges."""

texto = open("texto1.txt", encoding="utf-8").read()

print(len(texto))
linhas = texto.splitlines()
print("lns", len(linhas))
palavras = texto.split()
print("Palavras", len(palavras))

frases = texto.split(".")
print(len(frases))
