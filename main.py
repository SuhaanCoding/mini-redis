store={}
while True:
    cmd = input(">>>")
    if cmd.lower() == "exit":
        print("BYE BITCH")
        break
    else: 
        print(f"You typed {cmd}")
        parts = cmd.split()
        print(parts)
        if parts[0] == "SET":
            store[parts[1]] = parts[2]
            print("OK")


