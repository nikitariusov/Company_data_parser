from selenium import webdriver


def link_selection(url):

    input('\nДалее будет открыто окно, скопируйте нужную ссылку и закройте его.\n'
          'Для продолжения нажмите Enter...')

    browser = webdriver.Chrome('chromedriver')
    browser.get(url)

    link = input(str('Вставте скопированную ссылку: '))
    return link
