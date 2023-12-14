from lxml import etree

f = open( 'testamento.xml' )
tree = etree.parse(f)

for folha in tree.findall("//orig"):
    folha.tag = "sub"
for folha in tree.findall("//reg"):
    folha.tag = "sup"
    
tree.write("out.html", method="html", encoding="utf-8")

