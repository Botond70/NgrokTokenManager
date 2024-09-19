from os import system
import sys
counter = 0
#edit configpath for your instance
configpath = "C:/Users/boton/.ngrok2/ngrok.yml"

try:
    with open("c.txt",'r') as c:
        counter = int(c.read())
except:
    with open("c.txt",'w') as c:
        c.write("0")
    counter = 0
    
    
def loadbackup():
    counter = 0
    with open("tokenek.bac","r") as file:
        s = file.read()
        
        #print(tokens)
        print("loaded smthng ig\n")
        a = s.split(sep="\n")
        a.pop()
        return a
    
def load():
    counter = 0
    try:
        with open("tokenek.txt","r") as file:
            s = file.read()
            
            #print(tokens)
            print("loaded smthng ig\n")
            a = s.split(sep="\n")
            a.pop()
            #print(a)
            if a == []:
                a = loadbackup()
            return a
    except:
        return loadbackup()

    
def next(c,t):
    if len(t) > 0:
        c+=1
        c %= len(t)
        print("incremented counter, next token")
    else: print("error with incrementing")
    return c


    
def inject(ttt):
    """
    print("ngrok config add-authtoken " + ttt)
    system("ngrok config add-authtoken " + ttt)
    """
    with open(configpath,"w") as file:
        file.write("authtoken: " + ttt + "\nregion: eu\nversion: \"2\"\n")   
    
    return

    
def drop(c: int,t):
    t.pop(c)
    c %= len(t)
    return c,t
    
    
    
def main():
    with open("c.txt",'r') as c:
        counter = int(c.read())
    
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        tokens = load()
        try:
            arg2 = int(sys.argv[2])
        except:
            arg2 = 1
        if "b" in arg:
            counter = 0
            tokens = loadbackup()
            
        if "d" in arg:
            if len(sys.argv) > 2:
                drop(arg2,tokens)
                
            else:
                drop(counter,tokens)
                
        if "n" in arg:
            for i in range(arg2):
                counter = next(counter,tokens)
                print(counter,"\n")
                
        if "i" in arg: inject(tokens[counter])
        
    else:
        while ((command := input("Type: ")) != "q"):
            if command == "l":
                tokens = load()
                print(tokens)
            elif command == "n" : #next
                counter = next(counter,tokens)
                print(tokens[counter])
                print(counter,"\n")
                
            elif command == "i" : #inject token into ngrok
                inject(tokens[counter])
            elif command == "d": #drop current token
                drop(counter,tokens)

    
    print("\nlogging counter and tokens")
    with open("c.txt","w") as c:
        c.write(str(counter))
        
    with open("tokenek.txt","w") as t:
        for i in tokens:
            t.write(i+"\n")
    print("\n\nexiting program...\n")
    
    return 0

    
    
    
if __name__ == "__main__":
    main()

