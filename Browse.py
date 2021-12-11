from selenium import webdriver
from colorama import init, Fore, Style


def link_selection(url):
    try:
        input('\nДалее будет открыто окно браузера, скопируйте нужную ссылку и закройте его.\n'
              'Для продолжения нажмите Enter...')

        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])

        browser = webdriver.Chrome('chromedriver')
        browser.get(url)

        link = input(str('Вставьте скопированную ссылку: '))
        return link

    except:
        print(Fore.RED + '\n\t[ERROR] Возникла непредвиденная ошибка!')
        print('\nОткройте сайт вручную и скопируйте ссылку на нужную категорию.')
        link = input(str('Вставьте скопированную ссылку: '))
        print(Style.RESET_ALL)
        return link
