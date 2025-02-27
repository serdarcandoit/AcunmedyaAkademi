def main():
    
    calculator(1,2,"+")
    calculator(24,2,"-")
    calculator(13,3,"*")
    calculator(21,3,"/")
    calculator(17,21,"&")
    


def calculator(num1,num2,operator):
    list_of_operators = ["*","/","+","-"]

    if operator in list_of_operators:
        if operator == "+":
            print(f"{num1} + {num2} = {num1+num2}")
        elif operator == "-":
            print(f"{num1} - {num2} = {num1-num2}")
        elif operator == "*":
             print(f"{num1} * {num2} = {num1*num2}")
        else:
            if not num2 == 0:
                print(f"{num1} / {num2} = {num1/num2}")
            else:
                print("num2 can not be equal to 0!")
    else:
        print("Invalid operator")

    
main()