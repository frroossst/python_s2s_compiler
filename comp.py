import json
import re



class method():

    def __init__(self) -> None:
        pass

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
            # print(content)
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
    comp_content = None # currently not in use; only using source_content

    def __init__(self) -> None:
       compiler.source_content = method.readSource()

    def main(self):
  
        E = easterEggs()
        E.han_greedo()
        E.meaning_of_life()

        method.saveComp(compiler.source_content)



class easterEggs():

    def __init__(self) -> None:
        pass

    def han_greedo(self) -> None:
        pattern = "han shot first"
        repl = "greedo shot first"
        compiler.source_content = re.sub(pattern,repl,compiler.source_content,flags=re.IGNORECASE)

    def meaning_of_life(self) -> None:
        pattern0 = "what is the meaning of life"
        pattern1 = "answer to life the universe and everything"
        repl = "42"
        compiler.source_content = re.sub(pattern0,repl,compiler.source_content,flags=re.IGNORECASE)
        compiler.source_content = re.sub(pattern1,repl,compiler.source_content,flags=re.IGNORECASE)



if __name__ == "__main__":
    C = compiler()
    C.main()