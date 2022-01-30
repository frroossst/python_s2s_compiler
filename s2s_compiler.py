import random
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
        E.bakers_dozen()
        E.flip_a_coin()
        E.roll_a_die()
        E.roll_a_dnd_dice()
        E.error418()
        E.once_in_a_blue_moon()
        E.horns_of_unicorn()

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

    def bakers_dozen(self) -> None:
        pattern0 = "baker's dozen"
        pattern1 = "bakers dozen"
        repl = "13"
        compiler.source_content = re.sub(pattern0,repl,compiler.source_content,flags=re.IGNORECASE)
        compiler.source_content = re.sub(pattern1,repl,compiler.source_content,flags=re.IGNORECASE)

    def flip_a_coin(self) -> None:
        pattern = "flip a coin"
        coinFlip = ["heads","tails"]
        repl = random.choice(coinFlip)
        compiler.source_content = re.sub(pattern,repl,compiler.source_content,flags=re.IGNORECASE)
        
    def roll_a_die(self) -> None:
        pattern = "roll a die"
        dieRoll = ["1","2","3","4","5","6"]
        repl = random.choice(dieRoll)
        compiler.source_content = re.sub(pattern,repl,compiler.source_content,flags=re.IGNORECASE)

    def roll_a_dnd_dice(self) -> None:
        pattern = "roll a d20"
        dieRoll = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14",'15","16',"17","18","19","Nat 20"]
        repl = random.choice(dieRoll)
        compiler.source_content = re.sub(pattern,repl,compiler.source_content,flags=re.IGNORECASE)

    def error418(self) -> None:
        pattern = "Error 418"
        repl = "418. I'm a teapot \n The requested entity body is short and stout \n Tip me over and pour me out."
        compiler.source_content = re.sub(pattern,repl,compiler.source_content,flags=re.IGNORECASE)

    def once_in_a_blue_moon(self) -> None:
        pattern = "once in a blue moon"
        repl = "1.1669016 x 10e-8 hertz" 
        compiler.source_content = re.sub(pattern,repl,compiler.source_content,flags=re.IGNORECASE)

    def horns_of_unicorn(self) -> None:
        pattern = "the number of horns on a unicorn"
        repl = "1"
        compiler.source_content = re.sub(pattern,repl,compiler.source_content,flags=re.IGNORECASE)

    def loneliest_number(self) -> None:
        pass

    def anagram(self) -> None:
        pass

    def recursion(self) -> None:
        # randomly capitalize letters
        pass

    def pirate_language(self) -> None:
        pass

    def hacker_language(self) -> None:
        pass

    def loch_ness_monster(self) -> None:
        pass

    def funniest_joke(self) -> None:
        pattern = "Wenn ist das Nunstück git und Slotermeyer? Ja! Beiherhund das Oder die Flipperwaldt gersput! to English"
        repl = "[FATAL ERROR]"
        compiler.source_content = re.sub(pattern,repl,compiler.source_content,flags=re.IGNORECASE)

    def look_in_the_mirror(self) -> None:
        # reverse the whole doc string
        pass



if __name__ == "__main__":
    C = compiler()
    C.main()