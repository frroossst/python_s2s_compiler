
def barrelRoll():
    import time
    tag = "I suck at ascii art so here's the best I can do"
    anim = [" |", " /", " -", " \ "] * 10
    print(tag)
    for i in anim:
        time.sleep(0.25)
        print("Look at me do a barrel roll :",i,end="\r")
barrelRoll()
