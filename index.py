from turtle import home
from weakref import proxy
from markupsafe import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random
from data import user_settings_dict, username, password
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import instaloader
import random
import os
import time
from progress.bar import IncrementalBar
import eel

eel.init("web")

with open("proxy.txt") as inp:
    lines = inp.readlines()

random_proxy = random.choice(lines).strip()

proxie = {
    'http':f"{random_proxy}",
    'https':f"{random_proxy}"
}
proxie2 = {
    'http':f"{random_proxy}",
    'https':f"{random_proxy}"
}
proxie3 = {
    'http':f"{random_proxy}",
    'https':f"{random_proxy}"
}
proxie4 = {
    'http':f"{random_proxy}",
    'https':f"{random_proxy}"
}

# ----------------------------------------------------------------

print('''
██████╗░███████╗██╗░░░██╗███████╗██╗░░░░░░█████╗░██████╗░███████╗██████╗░  ░░░░░░
██╔══██╗██╔════╝██║░░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗██╔════╝██╔══██╗  ░░░░░░
██║░░██║█████╗░░╚██╗░██╔╝█████╗░░██║░░░░░██║░░██║██████╔╝█████╗░░██████╔╝  █████╗
██║░░██║██╔══╝░░░╚████╔╝░██╔══╝░░██║░░░░░██║░░██║██╔═══╝░██╔══╝░░██╔══██╗  ╚════╝
██████╔╝███████╗░░╚██╔╝░░███████╗███████╗╚█████╔╝██║░░░░░███████╗██║░░██║  ░░░░░░
╚═════╝░╚══════╝░░░╚═╝░░░╚══════╝╚══════╝░╚════╝░╚═╝░░░░░╚══════╝╚═╝░░╚═╝  ░░░░░░
██╗██╗░█████╗░██╗░░██╗██╗██╗██╗
╚█║╚█║██╔══██╗██║░██╔╝██║╚█║╚█║
░╚╝░╚╝██║░░██║█████═╝░██║░╚╝░╚╝
░░░░░░██║░░██║██╔═██╗░╚═╝░░░░░░
░░░░░░╚█████╔╝██║░╚██╗██╗░░░░░░
░░░░░░░╚════╝░╚═╝░░╚═╝╚═╝░░░░░░''')

print('Данная программа не нисет в себе ничего плохого и мы не заставляем использывать в плохих целях, с уважением разработчик - "Ok!"')
print('''P.S. - (Скрипт был разработан при поддержке программиста - "Ok!"
         Наш Discord: https://discord.gg/mxKZtFtMwp)''')
inp = ()

@eel.expose
def newdictuser(mask, login_us, pass_us):
    user_settings_dict.update({f'user_{mask}': {'login': f'{login_us}', 'password': f'{pass_us}'}})
    print(user_settings_dict)

@eel.expose
def take_py(txt_in):
    global inp
    inp = txt_in

# ----------------------------------------------------------------
home_button = "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div/div[1]/div/div[3]/div/div[1]/div/a"
L = instaloader.Instaloader()
follow_list = []
usem = ""
passe = ""

# Login or load session client
@eel.expose
def log(user__js, password__js):
    global usem
    global passe
    usem = f"{user__js}" # username данные от главного аккаунта откуда будем слизывать пользователей на которых ты подписался
    passe = f"{password__js}" # password
    L.login(usem, passe)
    # L2.context._session.proxies = proxie

    profile = instaloader.Profile.from_username(L.context, usem)
    global follow_list
    count = 0
    for followee in profile.get_followees():
        follow_list.append(followee.username)
        file = open("prada_followers.txt", "a+")
        file.write(follow_list[count])
        file.write("\n")
        file.close()
        bar = IncrementalBar('СБОР ПОДПИСОК', max = len(follow_list))
        for item in follow_list:
            bar.next()
        count = count + 1

    with open('prada_followers.txt') as file:
        follow_list = [row.strip() for row in file]
        

# usem2 = ""
# passe2 = ""
# L2.login(usem2, passe2)
# L2.context._session.proxies = proxie


# usem3 = ""
# passe3 = ""
# L3.login(usem3, passe3)
# L3.context._session.proxies = proxie2


# usem4 = ""
# passe4 = ""
# L4.login(usem4, passe4)
# L4.context._session.proxies = proxie3

# usem5 = ""
# passe5 = ""
# L1.login(usem5, passe5)
# L1.context._session.proxies = proxie4

class InstagramBot():
    def __init__(self, username, password):

        self.username = username
        self.password = password
        options = Options()
        options.add_argument('--headless')
        self.browser = webdriver.Chrome("./chromedriver/chromedriver.exe", options=options) # запуск нужного драйвера chrome
 
    # метод для закрытия браузера
    def close_browser(self):

        self.browser.close()
        self.browser.quit()

    # метод логина
    def login(self):

        browser = self.browser
        browser.get('https://www.instagram.com')
        time.sleep(random.randrange(3, 5))

        username_input = browser.find_element_by_name('username') # обращение к элементам инстаграма
        username_input.clear()
        username_input.send_keys(usem) # username проходят через цыкл в конце и записываются новыми значениями твинков через data

        time.sleep(2) # перерыв

        password_input = browser.find_element_by_name('password') # обращение к єлементам инстаграма
        password_input.clear()
        password_input.send_keys(passe) # password проходят через цыкл в конце и записываются новыми значениями твинков через data

        password_input.send_keys(Keys.ENTER)
        time.sleep(10)

    def xpath_exists(self, url):

        browser = self.browser
        try:
            browser.find_element_by_xpath(url)
            exist = True
        except NoSuchElementException:
            exist = False
        return exist

    def send__message(self, usernames="", message="", img_path=''):

        browser = self.browser
        time.sleep(random.randrange(2, 4))

        direct_message_button2 = "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a"

        if not self.xpath_exists(direct_message_button2):
            print("Кнопка отправки сообщений не найдена!")
            self.close_browser()
        else:
            print("Отправляем сообщение...")
            direct_message2 = browser.find_element_by_xpath(direct_message_button2).click()
            time.sleep(random.randrange(2, 4))

        send_message_button2 = browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div/div[2]/div/div/div[2]/div/div[3]/div/button").click()
        time.sleep(random.randrange(2, 4))

        # отправка сообщения нескольким пользователям
        # вводим получателя
        to_input2 = browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div[2]/input")
        to_input2.send_keys(follow_list[0])
        time.sleep(random.randrange(2, 7))

        # выбираем получателя из списка
        users_list2 = browser.find_element_by_xpath(
            "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div[2]").find_element_by_tag_name("button").click()
        time.sleep(random.randrange(2, 4))

        next_button2 = browser.find_element_by_xpath(
            "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[3]/div/button").click()
        time.sleep(5)

        # отправка текстового сообщения
        if message:
            text_message_area2 = browser.find_element_by_xpath(
                "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
            text_message_area2.clear()
            text_message_area2.send_keys(message)
            time.sleep(random.randrange(2, 4))
            text_message_area2.send_keys(Keys.ENTER)
            print(f"Сообщение для {usernames} успешно отправлено!")
            time.sleep(random.randrange(2, 4))
            if not self.xpath_exists(home_button):
                print("Кнопка Домой не найдена!")
                self.close_browser()
            else:
                print("Отправляемся домой...")
                home2 = browser.find_element(By.XPATH, home_button).click()
                time.sleep(20)

            for i in [0]:
                follow_list.pop(i)

            with open('prada_followers.txt', 'r') as f:
                lines = f.readlines()

            # запишем файл построчно пропустив первую строку
            with open('prada_followers.txt', 'w') as f:
                f.writelines(lines[1:])

            time.sleep(2)
            my_bot = InstagramBot(username, password)
            my_bot.send__message(follow_list, inp)

        # отправка изображения
        if img_path:
            send_img_input = browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/form/input")
            send_img_input.send_keys(img_path)
            print(f"Изображение для {usernames} успешно отправлено!")
            time.sleep(random.randrange(2, 4))

    def send_direct_message(self, usernames="", message="", img_path=''):

        browser = self.browser
        time.sleep(random.randrange(2, 4))

        direct_message_button = "/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[2]/a"

        if not self.xpath_exists(direct_message_button):
            print("Кнопка отправки сообщений не найдена!")
            self.close_browser()
        else:
            print("Отправляем сообщение...")
            direct_message = browser.find_element_by_xpath(direct_message_button).click()
            time.sleep(random.randrange(2, 4))

        # отключаем всплывающее окно
        if self.xpath_exists("/html/body/div[4]/div/div"):
            browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]").click()
        time.sleep(random.randrange(2, 4))

        send_message_button = browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div/div[2]/div/div/div[2]/div/div[3]/div/button").click()
        time.sleep(random.randrange(2, 4))

        # отправка сообщения нескольким пользователям
        # вводим получателя
        to_input = browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/div[2]/input")
        to_input.send_keys(follow_list[0])
        time.sleep(random.randrange(2, 7))

        # выбираем получателя из списка
        users_list = browser.find_element_by_xpath(
            "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div[2]").find_element_by_tag_name("button").click()
        time.sleep(random.randrange(2, 4))

        next_button = browser.find_element_by_xpath(
            "/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[3]/div/button").click()
        time.sleep(5)

        # отправка текстового сообщения
        if message:
            text_message_area = browser.find_element_by_xpath(
                "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
            text_message_area.clear()
            text_message_area.send_keys(message)
            time.sleep(random.randrange(2, 4))
            text_message_area.send_keys(Keys.ENTER)
            print(f"Сообщение для {usernames} успешно отправлено!")
            time.sleep(random.randrange(2, 4))
            if not self.xpath_exists(home_button):
                print("Кнопка Домой не найдена!")
                self.close_browser()
            else:
                print("Отправляемся домой...")
                home = browser.find_element(By.XPATH, home_button).click()
                time.sleep(10)

        # отправка изображения
        if img_path:
            send_img_input = browser.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/form/input")
            send_img_input.send_keys(img_path)
            print(f"Изображение для {usernames} успешно отправлено!")
            time.sleep(random.randrange(2, 4))

# for user, user_data in user_settings_dict.items(): # перебор пользователей из data
@eel.expose
def sta():
    for user, user_data in user_settings_dict.items():
        username = user_data['login']
        password = user_data['password']
        my_bot = InstagramBot(username, password)
        my_bot.login()
        my_bot.send_direct_message(follow_list, inp)
        time.sleep(random.randrange(4, 8))
        for i in [0]:
            follow_list.pop(i)

        with open('prada_followers.txt', 'r') as f:
            lines = f.readlines()
        # запишем файл построчно пропустив первую строку
        with open('prada_followers.txt', 'w') as f:
            f.writelines(lines[1:])

        my_bot.send__message(follow_list, inp)
eel.start("index.html")
