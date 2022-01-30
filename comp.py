import json
import re
import string
from sys import flags



class method():

    @classmethod
    def readSettings(self,type) -> str:
        # Reading file name from settings.json
        with open("settings.json","r") as fobj:
            settings = json.load(fobj)
            fobj.close() 

        if type == "fileName":
            fileName = settings["fileName"]
            return fileName

    @classmethod
    def readSource(self) -> str:
        # Reading soruce file contents
        with open(method.readSettings("fileName"),"r") as fobj:
            content = fobj.read()
            print(content)
            return content

    @classmethod
    def saveComp(self,result) -> None:
        # Writing to compiled file
        new_file = "comp_" + method.readSettings("fileName")
    
        # Writing contents to compiled file
        with open(new_file,"w") as fobj:
           fobj.write(result)



class compiler():

    source_content = None   
    comp_content = None

    def __init__(self) -> None:
       compiler.source_content = method.readSource()

    def main(self):
  
        E = easterEggs()
        E.han_greedo()

        method.saveComp(compiler.comp_content)


class easterEggs():

    def __init__(self) -> None:
        pass

    def han_greedo(self) -> None:
        pattern = "han shot first"
        repl = "greedo shot first"
        compiler.comp_content = re.sub(pattern,repl,compiler.source_content,flags=re.IGNORECASE)



C = compiler()
C.main()