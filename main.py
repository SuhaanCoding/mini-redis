store={}
while True:
    cmd = input(">>>")
    if cmd.lower() == "exit":
        print("BYE")
        break
    else: 
        print(f"You typed {cmd}")
        parts = cmd.split()
        print(parts)
        if parts[0] == "SET" and len(parts) == 3:
            store[parts[1]] = parts[2]
            print("OK")
        elif parts[0] == "GET" and len(parts) == 2:
            output = store.get(parts[1], "nil")
            print(output)
        elif parts[0] == "DEL" and len(parts) == 2:
            if parts[1] in store:
                temp = parts[1]
                temp2 = store.get(parts[1], "nil")
                del store[parts[1]]
                print(f"{temp} was deleted, and the content {temp2} inside it")
            else: print("NIL")
        else: print("The wrong command was inputted")


