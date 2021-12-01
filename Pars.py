from bs4 import BeautifulSoup
from Request import get_html, get_response


def pars_info(html_data):

    soup = BeautifulSoup(html_data, 'html.parser')
    cards_company = soup.find_all('div', class_='cart-company-lg')

    dict_keys = ["Название", "Сайт", "Почта", "Телефон",
                 "Вид деятельности"]

    data_base = []
    for card in cards_company:
        data_company = {}
        mail = card.find('a', target="_blank", rel=None)
        site = card.find('a', rel="nofollow", target="_blank")
        dict_value = []

        if mail:

            title = card.find('div', class_='cart-company-lg__title ui-title-inner')
            dict_value.append(title.text)

            if site:
                dict_value.append(site.text)
            else:
                dict_value.append("")

            dict_value.append(mail.text)

            phone = card.find('a', rel="nofollow", class_="text-nowrap")
            if phone:
                phone = phone.text
            else:
                phone = None
            dict_value.append(phone)

            categorys_card = card.find('ul', class_="ui-list-mark")
            categorys = categorys_card.find_all('a')

            category = []
            for i in categorys:
                content = i.text
                category.append(content)
            dict_value.append(category)

            n = 0
            for key in dict_keys:
                data_company[key] = dict_value[n]
                n += 1
            #print('[INFO] Дание о компании: ', data_company)
            data_base.append(data_company)

    return data_base


def pages(link, HEADERS):
    max_page = 1

    response = get_response(link, HEADERS)
    html_data = get_html(response)

    soup = BeautifulSoup(html_data, 'html.parser')

    paginations_class = soup.find('ul', class_='pagination')
    paginations = paginations_class.find_all('a', class_='item-link', text=True)

    if not paginations:
        return max_page
    else:
        max_page = int(paginations[-1].text)
        return max_page

