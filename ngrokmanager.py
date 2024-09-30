from os import system
import sys
counter = 0
#edit configpath for your instance
configpath = "C:/Users/{your_username}/.ngrok2/ngrok.yml"
region = "eu"
try:
    with open("counter.txt",'r') as c:
        counter = int(c.read())
except:
    with open("counter.txt",'w') as c:
        c.write("0")
    counter = 0
    
    
def loadbackup():
    #failsafe, the program also uses this function at the first start.
    counter = 0
    with open("tokens.bac","r") as file:
        string = file.read()
        
        #print(tokens)
        print("Loaded from backup.\n")
        splitString = string.split(sep="\n")
        splitString.pop()
        return splitString
    
def load():
    #The program loads the tokens from the savefile.
    counter = 0
    try:
        with open("tokens.txt","r") as file:
            string = file.read()
            
            #print(tokens)
            print("Loaded from savefile.\n")
            splitString = string.split(sep="\n")
            splitString.pop()
            #print(a)
            if splitString == []:
                splitString = loadbackup()
            return splitString
    except:
        return loadbackup()

    
def next(counter,tokens):
    #the program cycles through the list of tokens, with this function you can access the next token in the list.
    if len(tokens) > 0:
        counter+=1
        counter %= len(tokens)
        print("incremented counter, next token")
    else: print("error with incrementing")
    return counter


    
def inject(token):
    #injects the provided token inside the .yml file
    #a previous update broke the ngrok authtoken command, and this is how i fixed it.
    """
    print("ngrok config add-authtoken " + token)
    system("ngrok config add-authtoken " + token)
    """
    
    with open(configpath,"w") as file:
        file.write("authtoken: " + token + "\nregion: " + region + "\nversion: \"2\"\n")   
    
    return

    
def drop(counter: int,tokens):
    #drops nth token from the list, updates the counter accoridingly
    tokens.pop(c)
    counter %= len(tokens)
    return counter, tokens
    
    
    
def main():
    #imports counter from the last time the program ran.
    with open("counter.txt",'r') as c:
        counter = int(c.read())

    #if there were arguments present when the file ran: use the cli ui-less mode
    #if there werent. Use the text ui.
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        tokens = load()
        try:
            arg2 = int(sys.argv[2])
        except:
            arg2 = 1

        #b = load from backup
        if "b" in arg:
            counter = 0
            tokens = loadbackup()

        #d = drop arg2-th token
        if "d" in arg:
            if len(sys.argv) > 2:
                drop(arg2,tokens)
                
            else:
                drop(counter,tokens)
        #cycle onto next token
        if "n" in arg:
            for i in range(arg2):
                counter = next(counter,tokens)
                print(counter,"\n")
        #inject the last used token (from previous run)     
        if "i" in arg: inject(tokens[counter])
        
    else:
        #cli text ui mode
        #"q" quits the program and saves the counter, and updates the token list file ("tokens.txt").
        while ((command := input("Type: ")) != "q"):
            #load tokens
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

    #saves the counter, and tokens into their respective files.
    print("\nlogging counter and tokens")
    with open("counter.txt","w") as c:
        c.write(str(counter))
        
    with open("tokenek.txt","w") as t:
        for i in tokens:
            t.write(i+"\n")
    print("\n\nexiting program...\n")
    
    return 0

    
    
    
if __name__ == "__main__":
    main()

