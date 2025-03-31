def change():
    expense = 23.75
    money = 100
    vuelto= money - expense
    pesos=int(vuelto)
    print("Ingresar gasto:")
    print(f"{expense}")
    print("Dinero recibido")
    print(f"{money}\n")
    print("Vuelto\n")
    print("Pesos:")
    print(f"{pesos}")
    print("Centavos:")
    print(f"{int((vuelto-pesos)*100)}")
