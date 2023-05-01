from random import *

def loe_failist(f):
    file=open(f,'r',encoding="utf-8-sig")
    mas=[] 
    for rida in file:
        mas.append(rida.strip())
    file.close()
    return mas

def tolkimine(rus_list,est_list):
    ans=input("Sisestage sõna: ")
    if ans in rus_list:
        ind=rus_list.index(ans)
        print(f"{ans} on {est_list[ind]} eesti keeles")
    elif ans in est_list:
        ind=est_list.index(ans)
        print(f"{ans} on {rus_list[ind]} vene keeles")
    else:
        print(f"{ans} pole sõnastikud")


def save(f,text):  #funct dobavljaet slova v "lists", i ispolzuet funct "Loe_failist". then return result
    file=open(f,'a',encoding="utf-8-sig") #a - append
    file.write(text+"\n")
    file.close()
    mas=[]
    mas=loe_failist(f)
    return mas

def pop(f,text): 
    file=open(f,'a',encoding="utf-8-sig")
    file.remove(text+"\n")
    file.close()
    mas=[]
    mas=loe_failist(f)
    return mas

def add_sõna():  #soxranjaet slova kotorie vvel polzovateli, ispolzuja funct "save"
    rus_list=input("Sisesta sõna vene keeles:")
    est_list=input("Sisesta sõna eesti keeles:")
    rus_list=save("rus.txt",rus_list)
    est_list=save("est.txt",est_list)
    return est_list, rus_list


def update(rus_list,est_list):
    answer=input("Sisestage vale sõna: ")
    if answer in rus_list:
        ind=rus_list.index(answer)
        print(f"Paar sõna parandatakse {answer} - {est_list[ind]}")
        rus_list.pop(ind)
        est_list.pop(ind)
        a=input("Sisesta sõna vene keeles:")
        b=input("Sisesta sõna eesti keeles:")
        rus_list.append(a)
        est_list.append(b)
    elif answer in est_list:
        ind=est_list.index(answer)
        print(f"Paar sõna parandatakse {answer} - {rus_list[ind]}")
        rus_list.pop(ind)
        est_list.pop(ind)
        a=input("Sisesta sõna vene keeles:")
        b=input("Sisesta sõna eesti keeles:")
        rus_list.append(a)
        est_list.append(b)
    else:
        print(f"{answer.upper()} pole sõnastikus")
    rus_list=loe_failist("rus.txt")
    est_list=loe_failist("est.txt")
    return rus_list,est_list


def game(rus_list,est_list):
    o=e=0
    v=int(input("Kui palju raundi: "))
    lang=int(input("Mis keel.(1-vene,2-est)"))
    for i in range(v):
        r=randint(0,len(rus_list)-1)
        if lang==1:
            anss=input(f"Kuidas tõlkida {rus_list[r]} ")
            if anss==est_list[r]:
                print("Õige")
                o+=1
            else:
                print("Vale")
                e+=1
        elif lang==2:
            anss=input(f"Kuidas tõlkida {est_list[r]} ")
            if anss==rus_list[r]:
                print("Õige")
                o+=1
            else:
                print("Vale")
                e+=1
    oige=o*100//v
    vale=e*100//v
    print(f"Õigete sõnade protsent - {oige}%")
    print(f"Valede sõnade protsent - {vale}%")
