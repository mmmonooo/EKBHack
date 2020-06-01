from firebase import Firebase
import hack
import os
import time

Config = {
    apiKey: "AIzaSyD-eyUwNCWOeT5uXJ4sJZvUDAZU4QGUB-0",
    authDomain: "bdkhack-a1b1f.firebaseapp.com",
    databaseURL: "https://bdkhack-a1b1f.firebaseio.com",
    storageBucket: "bdkhack-a1b1f.appspot.com"
  }
firebase = Firebase(Config)
auth = firebase.auth()
db = firebase.database()


def menuru():
    os.system('cls')
    print("BDK HACK")
    print("МЕНЮ:\n1 - Взлом сервера\n2 - Приобрести ключ\n3 - Поддержка\n4 - Разработчики\nMONO©")
    select = input('')
    if select == '4':
        while True:
            os.system('cls')
            print('Весь код писали MONO.\n1 - Группа\n2 - Разработчик в ВК\n3 - Назад')
            select4 = input('')
            if select4 == '1':
                os.system('start https://www.vk.com/monovk')
            if select4 == '2':
                os.system('start https://www.vk.com/mur4ikofficial')
            if select4 == '3':
                break
                restart()
    if select == '3':
        os.system('cls')
        print('Вопросы в лс группы MONO -> https://www.vk.com/monovk')
    if select == '2':
        os.system('cls')
        print("Купить ключ:\n1. Написать боту в VK -> https://vk.com/monovk\n2. Перейти в Меню->Наши приложения->BDK HACK->Купить ключ 3. Оплатите 239 рублей\n4.Мы отправим вам ключ.")
        print("Страница исчезнет через минуту")
        time.sleep(60)
        restart()
    if select == '1':
        os.system('cls')
        host = input("IP:")
        port = input("Порт:")
        ver = input("Версия (пример: 1.12.2):")
        hack.hack(host, port, ver)

def menuen():
    os.system('cls')
    print("BDK HACK")
    print("MENU:\n1 - Hack server\n2 - Buy a license key\n3 - Support\n4 - Developers\nMONO©")
    select = input('')
    if select == '4':
        while True:
            os.system('cls')
            print('All code writted by MONO.\n1 - Group VK\n2 - Developer on VK\n3 - Back')
            select4 = input('')
            if select4 == '1':
                os.system('start https://www.vk.com/monovk')
            if select4 == '2':
                os.system('start https://www.vk.com/mur4ikofficial')
            if select4 == '3':
                break
                restart()
    if select == '3':
        os.system('cls')
        print('Support -> https://www.vk.com/monovk')
    if select == '2':
        os.system('cls')
        print("Buy a license key:\n1. Write to bot -> https://vk.com/monovk\n2. Go to Меню->Наши приложения->BDK Hack->Купить ключ\n3. Pay 239P\n4. We will give you a license key.")
        print("You will go to menu in 60 seconds")
        time.sleep(60)
        restart()
    if select == '1':
        os.system('cls')
        host = input("IP:")
        port = input("Port:")
        ver = input("Version (example: 1.12.2):")
        hack.hack(host, port, ver)

def restart():
    menuru()

print("BDK Hack created by MONO")
email = input("Email: ")
password = input("Password: ")
try:
    auth.sign_in_with_email_and_password(email, password)
    print("Success!")
    lang = input("Select language [ru/en]:")
    if lang == 'ru':
        menuru()
    elif lang == 'en':
        menuen()
except:
    print("Error! Incorrect email or password!")
    print("Program will close in 5 seconds")
    time.sleep(5)
    quit()
