#!/usr/bin/python3

import json, sys, re
## json.dump(p,f)  json.dumps(p)  json.load(f) json.loads(str)

with open('ex1.json',encoding="utf8") as f:
    content = json.load(f)

print(content)

"""
#def mkjson(x): return json.dumps(x,ensure_ascii=False,indent=3)

def main():
   txt = open(sys.argv[1]).read()
   meta,*exs= re.split(r'\n\*\*',txt)       ## divide por exerc.
   dmeta= yaml.load(meta)

   for exer in exs:
       dexer=parse_exer(exer)
       print(mkjson({**dmeta,**dexer}))
===

json.loads(str)

with open('some/path.json', 'w') as f:
    json.dump({'foo': 'bar'}, f)

"""
