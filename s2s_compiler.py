from errno import ENETDOWN
import random
import json
import re



class method():

    def __init__(self) -> None:
        pass

    @classmethod
    def readSettings(self,type) -> str:
        # Reading file name from settings.json
        try:
            with open("settings.json","r") as fobj:
                settings = json.load(fobj)
                fobj.close() 

            if type == "fileName":
                fileName = settings["fileName"]
                if fileName == "":
                    fileName = settings["filePath"]        
                return fileName
            elif type == "changeSource":
                return settings["changeSource"]
        except:
            raise FileNotFoundError("settings.json not found")

    @classmethod
    def readSource(self) -> str:
        # Reading soruce file contents
        try:
            with open(method.readSettings("fileName"),"r") as fobj:
                content = fobj.read()
                return content
        except:
            raise FileNotFoundError ("could not locate source file")

    @classmethod
    def saveComp(self) -> None:
        # Writing to compiled file
        
        with open("settings.json","r") as fobj:
            settings = json.load(fobj)

        if settings["changeSource"]: # Source is changed itself 
            with open(method.readSettings("fileName"),"w") as fobj:
                fobj.write(compiler.source_content)
                fobj.close()
        elif not (settings["changeSource"]): # A new comp_ file is created``
            filePath = method.readSettings("fileName")
            pos = filePath.rfind("/") + 1
            fileName = filePath[pos:] 
            new_file = "comp_" + fileName
            
            with open(new_file,"w") as fobj:
                fobj.write(compiler.source_content)
                fobj.close()

    @classmethod 
    def cleanup(self):
        import os
        filesCreated = ["barrelRoll.py","vowelCount.json"]
        try: 
            for i in filesCreated:
                os.remove(i)
        except:
            pass

    @classmethod
    def cleanup_specialCharacters(self,str) -> str:
        specialCharacters = [",","!","?","<",">"]
        returnStr = ""

        for i in str:
            if i not in specialCharacters:
                returnStr += i
        
        return returnStr

    @classmethod
    def bracketMatch(self) -> None:
        content = method.readSource()
        openPara = content.count("(")
        closedPara = content.count(")")
        openCurl = content.count("{")
        closedCurl = content.count("}")
        openSquare = content.count("[")
        closedSquare = content.count("]")

        if (closedPara != openPara) or (openCurl != closedCurl) or (openSquare != closedSquare):
            raise SyntaxError ("Unmatching brackets")



class compiler():

    source_content = None   
    comp_content = None # currently not in use; only using source_content

    def __init__(self) -> None:
        method.cleanup()
        compiler.source_content = method.readSource()
        method.bracketMatch()

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
        E.look_in_the_mirror()
        E.mirrors_suck()
        E.do_a_barrel_roll()
        E.innit()

        method.saveComp()

        F = functional()
        F.not_remainder() 
        F.equal_remainder()
        F.forcedELIF()
        F.count_vowels()
        F.number_magic()

        method.saveComp()



class easterEggs():

    american_british_dict = {"airplane" : "aeroplane","cilantro" : "corriander", "eggplant" : "aubergine", "color" : "colour", "flavor" : "flavour",
    "humor" : "humour", "labor" : "labour", "neighbor" : "neighbour", "apologize" : "apologise", "organize" : "organise", "recognize" : "recognise",
    "behavior" : "behaviour", "analyze" : "analyse", "paralyze" : "paralyse", "defense" : "defence", "license" : "licence", "offense" : "offence",
    "analog" : "anologue", "dialog" : "dialogue", "mold" : "mould", "meter" : "metre", "fiber" : "fibre", "tire" : "tyre"}

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
        pattern = "what is the loneliest number"
        repl = "1"
        compiler.source_content = re.sub(pattern,repl,compiler.source_content,flags=re.IGNORECASE)

    def anagram(self) -> None:
        pattern = "anagram"
        repl = "nag a ram"
        compiler.source_content = re.sub(pattern,repl,compiler.source_content,flags=re.IGNORECASE)

    def recursion(self) -> None:
        # randomly capitalize letters
        pattern = "recursion"
        capital = random.sample(range(0,len(pattern)),4)
        repl = ""
        for index, i in enumerate(pattern):
            if index in capital:
                repl += i.upper()
            else:
                repl += i
        compiler.source_content = re.sub(pattern,repl,compiler.source_content,flags=re.IGNORECASE)

    def hacker_language(self) -> None:
        pass

    def loch_ness_monster(self) -> None:
        pattern = "where is the loch ness monster"
        repl = "you can find Nessie at 57.323667970003704, -4.424191149125835 \n Also he is not a monster!"
        compiler.source_content = re.sub(pattern,repl,compiler.source_content,flags=re.IGNORECASE)

    def funniest_joke(self) -> None:
        pattern = "Wenn ist das Nunstück git und Slotermeyer? Ja! Beiherhund das Oder die Flipperwaldt gersput! to English"
        repl = "[FATAL ERROR]"
        compiler.source_content = re.sub(pattern,repl,compiler.source_content,flags=re.IGNORECASE)

    def look_in_the_mirror(self) -> None:
        # reverse the whole doc string
        matchStatus = re.findall("I want to look in the mirror",compiler.source_content,flags=re.IGNORECASE)
        if matchStatus != None:
            if matchStatus!= []:
                compiler.source_content = compiler.source_content[::-1]
                if method.readSettings("changeSource"):
                    method.saveComp() 
                else:
                    method.saveComp()
                quit()
        else:
            pass

    def mirrors_suck(self) -> None:
        str = "mirrors suck"
        matchStatus = re.findall(str,compiler.source_content)
        keywords = ["print("]
        keywordStatus = False

        for i in keywords:
            if i in compiler.source_content:
                keywordStatus = True
                break

        if matchStatus != None and matchStatus!=[] and not keywordStatus:
            compiler.source_content = compiler.source_content[::-1] 
            if method.readSettings("changeSource"):
                method.saveComp()
            else:
                method.saveComp()
            quit()

    def do_a_barrel_roll(self) -> None:
        # write a function to a separate file and then replace the source print statement with an import statement  
        funcDef = """
def barrelRoll():
    import time
    tag = "I suck at ascii art so here's the best I can do"
    anim = [" |", " /", " -", " \\ "] * 10
    print(tag)
    for i in anim:
        time.sleep(0.25)
        print("Look at me do a barrel roll :",i,end="\\r")
        """

        repl = """import barrelRoll \nbarrelRoll.barrelRoll()"""
        pattern = '"do a barrel roll"'
        compiler.source_content = re.sub(pattern,repl,compiler.source_content,flags=re.IGNORECASE)

        with open("barrelRoll.py","w") as fobj:
            fobj.writelines(funcDef)

    def negative_zero(self) -> None:
        pass

    def innit(self) -> None:
        # american to british english
        # ! Does not work 
        for key, value in easterEggs.american_british_dict.items():
            compiler.source_content = re.sub(value,key,compiler.source_content,flags=re.IGNORECASE)
            method.saveComp()



    def yankee(self) -> None:
        # british to american englilsh
        pass





class functional():

    def __init__(self) -> None:
        pass

    def not_remainder(self) -> None:

        """ !% => not remainder
        Syntax => "a !% b,c;" translates to a % b != c
        """
        # TODO : Make it also work with variable names and not only numbers
        # ! Only works with numbers as of now, as it is only a partial evaluator and not a full interpreter.
        
        loopTotal = compiler.source_content.count("!%")
        loopCount = 0
        try:
            while True:
                if loopCount > loopTotal:
                    break
                loopCount += 1
                symbol = "!%"
                expression0 = []
                expression1 = []

                if symbol not in compiler.source_content:
                    break
                # Finding expressions
                lineCount = 0
                for i in range(0,len(compiler.source_content)-1):
                    curr_pointer = compiler.source_content[i] + compiler.source_content[i+1]
                    if compiler.source_content[i] == "\n":
                        lineCount += 1
                    if curr_pointer == symbol:
                        index = i
                        break

                # Loop backwards
                curr_index_B = index 
                while True:
                    startLine = ["\n", "="]
                    if compiler.source_content[curr_index_B] not in startLine:
                        expression0.append(compiler.source_content[curr_index_B])
                        curr_index_B -= 1
                    else:
                        expression0.reverse()
                        break
                    
                # Loop forwards
                curr_index_F = index
                while True:
                    if compiler.source_content[curr_index_F] != "\n":
                        expression1.append(compiler.source_content[curr_index_F])
                        curr_index_F += 1
                    else:
                        break

                # Seperating expression into componenets
                expression = expression0
                expression.pop()
                expression.extend(expression1)
                expressionStr = "".join(expression)

                dividend = None
                divisor = None
                remainder = None
                curr = ""

                for i in expressionStr:
                    if i.isdigit():
                        curr += i
                    else:
                        try:
                            if dividend == None:
                                dividend = int(curr)
                            elif divisor == None:
                                divisor = int(curr)
                            elif remainder == None:
                                remainder = int(curr)
                        except:
                            pass
                        curr = ""

                # Evaluating the expression using traditional python syntax
                if dividend % divisor != remainder:
                    evaluated = True
                else:
                    evaluated = False
                
                # Writing to the save file
                if evaluated != None:
                    compiler.source_content = re.sub(expressionStr,str(evaluated),compiler.source_content,flags=re.IGNORECASE)


        except:
            raise SyntaxError (f"Check syntax for  '{expressionStr}' in {method.readSettings('fileName')} at line {lineCount}")


    def equal_remainder(self) -> None:

        """ =% => equal remainder
        Syntax => "a =% b,c;" translates to a % b == c
        """
        # TODO : Make it also work with variable names and not only numbers
        # ! Only works with numbers as of now, as it is only a partial evaluator and not a full interpreter.
        
        loopTotal = compiler.source_content.count("=%")
        loopCount = 0
        try:
            while True:
                if loopCount > loopTotal:
                    break
                loopCount += 1
                symbol = "=%"
                expression0 = []
                expression1 = []

                if symbol not in compiler.source_content:
                    break
                # Finding expressions
                lineCount = 0
                for i in range(0,len(compiler.source_content)-1):
                    curr_pointer = compiler.source_content[i] + compiler.source_content[i+1]
                    if compiler.source_content[i] == "\n":
                        lineCount += 1
                    if curr_pointer == symbol:
                        index = i
                        break

                # Loop backwards
                curr_index_B = index 
                while True:
                    startLine = ["\n"]
                    if compiler.source_content[curr_index_B] not in startLine:
                        expression0.append(compiler.source_content[curr_index_B])
                        curr_index_B -= 1
                    else:
                        expression0.reverse()
                        break
                    
                # Loop forwards
                curr_index_F = index
                while True:
                    if compiler.source_content[curr_index_F] != "\n":
                        expression1.append(compiler.source_content[curr_index_F])
                        curr_index_F += 1
                    else:
                        break

                # Seperating expression into componenets
                expression = expression0
                expression.pop()
                expression.extend(expression1)
                expressionStr = "".join(expression)

                dividend = None
                divisor = None
                remainder = None
                curr = ""

                for i in expressionStr:
                    if i.isdigit():
                        curr += i
                    else:
                        try:
                            if dividend == None:
                                dividend = int(curr)
                            elif divisor == None:
                                divisor = int(curr)
                            elif remainder == None:
                                remainder = int(curr)
                        except:
                            pass
                        curr = ""

                # Evaluating the expression using traditional python syntax
                if dividend % divisor != remainder:
                    evaluated = True
                else:
                    evaluated = False
                
                # Writing to the save file
                if evaluated != None:
                    compiler.source_content = re.sub(expressionStr,str(evaluated),compiler.source_content,flags=re.IGNORECASE)


        except:
            raise SyntaxError (f"Check syntax for  '{expressionStr}' in {method.readSettings('fileName')} at line {lineCount}")

    def forcedELIF(self) -> None:

        startFlag = "FORCED{"
        endFlag = "}"
        
        try:
            while True:
                if startFlag not in compiler.source_content:
                    break
                
                for i in range(0,len(compiler.source_content)):
                    curr_pointer = compiler.source_content[i] + compiler.source_content[i+1] + compiler.source_content[i+2] + compiler.source_content[i+3] + compiler.source_content[i+4] + compiler.source_content[i+5] + compiler.source_content[i+6]
                    if curr_pointer == startFlag:
                        index = i
                        break
                
                count = index
                substring = []
                while True:
                    
                    if compiler.source_content[count] == endFlag:
                        substring.append(compiler.source_content[count])
                        endex = count
                        break

                    substring.append(compiler.source_content[count])
                    count += 1


                substring = "".join(substring)
                modstring = substring
                # Replacing elif with if statements
                pattern = "elif"
                repl = "if"
                modstring = re.sub(pattern,repl,modstring)
                # Removing non syntax elements
                pattern = startFlag
                repl = ""
                modstring = re.sub(pattern,repl,modstring)
                pattern = endFlag
                repl = ""
                modstring= re.sub(pattern,repl,modstring)

                # Writing to source_content
                compiler.source_content = compiler.source_content[:index] + modstring + compiler.source_content[endex+1:]

        except Exception as e:
            print(e)

    def count_vowels(self) -> None:

        vowels = ["a","e","i","o","u"]
        hash_vowels = {"a" : 0, "e" : 0, "i" : 0, "o" : 0, "u" :0}

        symbol = ".countVowels"

        try:
            while True:
                if symbol not in compiler.source_content:
                    break

                for i in range(0,len(compiler.source_content)):
                    if i + 12 > len(compiler.source_content):
                        break
                    curr_pointer = (compiler.source_content[i] + compiler.source_content[i+1] + compiler.source_content[i+2] + 
                    compiler.source_content[i+3] + compiler.source_content[i+4] + compiler.source_content[i+5] + compiler.source_content[i+6] +  
                    compiler.source_content[i+7] + compiler.source_content[i+8] + compiler.source_content[i+9] + compiler.source_content[i+10] +
                    compiler.source_content[i+11])
                    
                    if curr_pointer == symbol:
                        index = i

                        flagCount = 0
                        substring = []
                        while True:
                            if flagCount == 2:
                                break
                            
                            sq = False
                            dq = False

                            if compiler.source_content[index] == "\'":
                                sq = True
                            if compiler.source_content[index] == "\"":
                                dq = True

                            if (compiler.source_content[index] == "\'" and sq) or (compiler.source_content[index] == "\"" and dq):
                                substring.append(compiler.source_content[index])
                                flagCount += 1
                            index -= 1

                        text = "".join(substring)
                        print(text)

                        for i in text:
                            if i in vowels:
                                hash_vowels[i] += 1
                        break
                break

        except Exception as e:
            print(e)
        
    def bruteSort(self) -> None:
        # Sorts a mixed string and numerical list
        # List needs to be explicitly defined or passed as arguments
        # Syntax => 
        # li = [1,2,"a","b",3,"c"]
        # li.bruteSort()
        # Output => ["a","b","c",1,2,3] (alpha=True)
        # Output => [1,2,3,"a","b","c"] (alpha=False)
        
        # TODO : For partial evaluation add comments and execute and save outout and then remove comments
        symbol = "bruteSort("

    

    def system_of_linear_equation(self) -> None:
        pass

    def number_magic(self) -> None:
        numDict = {"one" : 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9, "ten" : 10,
        "eleven" : 11, "twelve" : 12, "thirteen" : 13, "fourteen" : 14, "fifteen" : 15, "sixteen" : 16, "seventeen" : 17, "eighteen" : 18,
        "nineteen" : 19, "twenty" : 20, "thirty" : 30, "fourty" : 40, "fifty" : 50, "sixty" : 60, "seventy" : 70, "eighty" : 80, "ninety" : 90,
        "hundred" : 100, "thousand" : 1000, "million" : 100000000, "billion" : 100000000000, "trillion" : 100000000000000}

        symbol = "NUMBER{"
        endFlag = "}"

        try:
            while True:
                if symbol not in compiler.source_content:
                    break
                
                for i in range(0,len(compiler.source_content)):
                    curr_pointer = (compiler.source_content[i] + compiler.source_content[i+1] + compiler.source_content[i+2] + 
                    compiler.source_content[i+3] + compiler.source_content[i+4] + compiler.source_content[i+5] + compiler.source_content[i+6])
                    if curr_pointer == symbol:
                        index = i
                        break
                
                expression = []
                while True:
                    if compiler.source_content[index] != endFlag:
                        expression.append(compiler.source_content[index])
                        index += 1
                    else:
                        break

                expressionStr = "".join(expression)
                expressionStr = expressionStr[7:]
                print(expressionStr) 

                # Decoding the expression


        except:
            pass











if __name__ == "__main__":
    C = compiler()
    C.main()