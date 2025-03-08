def main():
    

    for i in range(5):
        
        line = input(f"{i+1}. line: ")
        with open("text.txt","a") as file:
            file.write(f"{line}\n")
        

    with open("text.txt","r") as file:
        lines = file.read()
        for line in lines:
            print(line,end="")



main()