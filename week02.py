# 1) Ice Americano : 2000 2) Cafe latte : 3000
prices=[2000,3000]
drinks=["Ice Americano","Cafe Latte"]
while True:

    menu = input(f"1) {drinks[0]} {prices[0]}won 2) {drinks[1]}{prices[1]} 3) Exit :")
    if menu=="1":
        print(f"Ice Americano ordered. Price :{prices[0]} won")

    elif menu=="2":
        print(f"Cafe latte ordered. Price : {prices[1]}won")

    elif menu=="3":
        print("Finish order~")
        break


    else:
        print(f"{menu} menu is not exist.please choose from above menu")