senha=1234
i=0
pin=0
while i!=3 or pin!=senha:
    pin = int(input("digite uma senha de 4 digitos: "))
    if i==3:
        print("numero de tentativas execedidas")
        break
    else:
        if pin==senha:
            print("correta")
            break