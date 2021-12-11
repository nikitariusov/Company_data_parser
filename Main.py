""" Документация:
Программа предназначена для парсинга данных о компаниях в Украине.
Цель: собрать электронные почты, телефоны, адреса сайтов, для рассылки информации и рекламы.
Парсинг происходит с сайта https://www.ua-region.com.ua/.
_________________________________________________

Релиз (v.1.0):
1. Получить ссылку через браузер или использовать все ссылки что внесены в базу;
2. Переход по каждой ссылке;
3. Сбор информации со страницы списка организаций:
    3.1 Сбор только если указанна электронная почта;
    3.2 Сбор: Название, Сайт, Почта, Телефоны, Вид деятельности, Категория/подкаиегория;
4. Сохранение всех данных в ексель;
5. Вывод времени работы скрипта;
_________________________________________________

Архитектура:
1. Main - Главная программа;
2. Request - отправка/получение ответа с сервера;
3. Browse - Выбор одной ссылки через открытие браузера;
4. Pars - Разбор страницы html, сбор и сохранение данных в словарь;
5. Recording - Создание Excel файла и запись всех данных.
"""


from Request import get_response, get_html
from Pars import pars_info, pages
from Browse import link_selection
from Recording import recording_on_file
from colorama import init, Fore
import time

init()
URL = 'https://www.ua-region.com.ua/ru/biznes-katalog'
HOST = 'https://www.ua-region.com.ua/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/90.0.4430.212 Safari/537.36', 'accept': '*/*'}

""" ----- Список всех ссылок ----- """
selhoz = ["https://www.ua-region.com.ua/ru/kved/01.11", "https://www.ua-region.com.ua/ru/kved/01.12",
          "https://www.ua-region.com.ua/ru/kved/01.13",  ]

list_links = [selhoz, ]


def script_execution_time():
    runtime = time.time() - start_time
    print(f"[INFO] Время выполнения: {'{0:.2f}'.format(runtime)}c.")


def status_1():
    print('[STATUS] Сбор пагинации...')


def user_selection():
    """Выбор метода определения ссылок"""
    print("Вы можете выбрать парсинг по всем категориям сразу, или выбрать нужную категорию "
          "скопировав ссылку на нее.")
    variant = input('Введите 1 - парсинг по всем категориям;\n'
                    'Введите 2 - открыть браузер и выбрать категорию;\n'
                    'Введите q - выйти из программы.\n'
                    'Ваш выбор: ')
    return variant


def get_pagination(first_link):
    pagination = pages(first_link, HEADERS)

    max_page_link = first_link + '?start_page=' + str(pagination)

    if pagination == 1:
        return max_page_link

    else:
        check_pagination = pages(max_page_link, HEADERS)
        while pagination <= check_pagination:
            pagination = check_pagination
            max_page_link = first_link + '?start_page=' + str(pagination)
            check_pagination = pages(max_page_link, HEADERS)

        print('[INFO] Количество пагинации: ', pagination, 'страниц.')

        links_page = []
        for i in range(1, pagination + 1):
            link_page = first_link + '?start_page=' + str(i)
            links_page.append(link_page)

        return links_page


def main():
    global start_time
    #variant = user_selection()
    variant = "2"
    all_links = []
    if variant == "1":
        start_time = time.time()
        status_1()
        for links in list_links:

            for link in links:
                paginations_links = get_pagination(link)
                for pagination_link in paginations_links:
                    all_links.append(pagination_link)

            print('[INFO] Все ссылки: ', all_links)

        all_data_base = []

        for link in all_links:
            #print('[INFO] Передана ссылка: ', link)
            response = get_response(link, HEADERS)
            html_data = get_html(response)

            print('[STATUS] Сбор данных со страницы: ', link)
            data = pars_info(html_data)

            if len(data) > 0:
                print('[INFO] Передан словарь с данными: ', data)
                all_data_base += data

        print('[INFO] Вся база: ', all_data_base)
        print("\n[INFO] Количество записей: ", len(all_data_base))

        recording_on_file(all_data_base)

    if variant == "2":
        start_time = time.time()
        link = link_selection(URL)
        #link = 'https://www.ua-region.com.ua/ru/kved/05.10'
        print('[STATUS] Ждите, идет сбор кол-ва страниц...')
        paginations_links = get_pagination(link)

        all_data_base = []

        for link in paginations_links:
            #print('[INFO] Передана ссылка: ', link)
            response = get_response(link, HEADERS)
            html_data = get_html(response)

            print('[STATUS] Сбор данных со страницы:', link)
            data = pars_info(html_data)

            if len(data) > 0:
                #print('[INFO] Передан словарь с данными: ', data)
                all_data_base += data

        print('\n[INFO] Вся база: ', all_data_base)
        print("\n[INFO] Количество записей: ", len(all_data_base))

        recording_on_file(all_data_base)

    if variant == 'q':
        quit()


main()
script_execution_time()
input()
quit()
