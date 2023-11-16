#!/usr/bin/env python

""" extrair nomes proprios Vanessa, Vanessa da Silva
um por linha

  -a    anotação

NP = ( PM _ ) +
PM = Ll+
"""
from jjcli import * 
from collections import Counter

cl=clfilter("a", doc= __doc__ )    ## option values in cl.opt dictionary

# expressoes regulares
PM = r'([A-ZÁÉÍÓÚÂÊÔ]\w+)'     # vai panhar falsos positivos F16 F3m
# NP = r'(([A-ZÁÉÍÓÚÂÊÔ]\w+ )+)' # P_  P_P_  
# NP = fr'({PM} )+)'             # P_  P_P_  
# NP = fr'({PM}( {PM})*)'          # P  P_P P_P_P  
NP = fr'({PM}( {PM}| d[eao] {PM})*)' # P  P_P P_de_P  P_P_P  

oco = Counter()
for txt in cl.text():    
     if "-a" in cl.opt:
        txt = re.sub( NP, r'<N>\1</N>', txt)
        print(txt)
     else:
        for n, n2,n3,n4,n5 in findall(NP,txt):
            oco[n] += 1
        print(oco)




