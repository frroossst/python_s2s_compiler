import json
import re

# Reading file name from settings.json
with open("settings.json","r") as fobj:
    settings = json.load(fobj)
    fobj.close() 

fileName = settings["fileName"]

# Reading soruce file contents
with open(fileName,"r") as fobj:
    content = fobj.read()
    print(content)

# Testing out RegEx
pattern = "han shot first"
repl = "greedo shot first"
result = re.sub(pattern,repl,content)
print(result)

# Writing to compiled file
new_file = "comp_" + fileName 

# Writing contents to compiled file
with open(new_file,"w") as fobj:
    fobj.write(result)