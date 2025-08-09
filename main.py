store={}
while True:
    cmd = input(">>>")
    if cmd.lower() == "exit":
        print("BYE")
        break
    else: 
        print(f"You typed {cmd}")
        parts = cmd.split(maxsplit = 2)
        if not parts:
            continue
        parts[0] = parts[0].upper()
        if parts[0] == "SET":
            if len(parts) == 3:
                store[parts[1]] = parts[2]
                print("Stored the Parts")
            elif len(parts) > 3:
                parts2 = cmd.split(maxsplit = 2)
                store[parts2[1]] = parts2[2]
            else: print("Wrong Number of Arguments")


        elif parts[0] == "GET":
            if len(parts) == 2:
                output = store.get(parts[1], "nil")
                print(output)
            else: print("Wrong Number of Arguments")

        elif parts[0] == "DEL":
            if len(parts) == 2:
                if parts[1] in store:
                    temp = parts[1]
                    temp2 = store.get(parts[1], "nil")
                    del store[parts[1]]
                    print(f"{temp} was deleted, and the content {temp2} inside it")
                else: print("NIL")
            else: print("Wrong Number of Arguments")
        
        elif parts[0] == "KEYS":
            if len(parts) == 1:
                print(" ".join(store.keys()))
            else: print("Wrong number of arguments")

        elif parts[0] == "EXISTS":
            if len(parts) ==2 : 
                print(1 if parts[1] in store else 0)
            else: print("Wrong Number of Arguments Inputted")
        else: print("The wrong command was inputted")



