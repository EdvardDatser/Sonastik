from modul import *


rus_list=loe_failist("rus.txt")
est_list=loe_failist("est.txt")
print(rus_list)
print(est_list)
while True:
    menu = int(input("0 - Sule menu\n1 - Tõlkimine\n2 - Uus sõna\n3 - Veaparandus\n4-Mäng"))
    if menu == 1:
        tolkimine(rus_list,est_list)
    elif menu == 0:
        break
    elif menu == 2:
        rus_list,est_list = add_sõna()
        print(rus_list)
        print(est_list)
    elif menu == 3:
        print(rus_list,est_list)
        update(rus_list,est_list)
        print(rus_list,est_list)
    elif menu == 4:
        game(rus_list,est_list)
