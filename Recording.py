from openpyxl import Workbook
from colorama import init, Fore

def recording_on_file(data):

    dict_keys = ["Название", "Сайт", "Почта", "Телефон",
                 "Вид деятельности"]

    wb = Workbook()
    file_name = "Data.xlsx"
    ws1 = wb.active
    ws1.title = "Data_base"

#       Создаем шапку
    n = 0
    row = ["A", "B", "C","D","E"]
    for j in row:
        ws1[f'{j}1'] = dict_keys[n]
        n += 1

#       Запись контента
    row = 2
    for company_data in data:
        ws1[f'A{row}'] = company_data['Название']
        ws1[f'B{row}'] = company_data['Сайт']
        ws1[f'C{row}'] = company_data['Почта']
        if company_data['Телефон']:
            ws1[f'D{row}'] = company_data['Телефон'].strip()

        content = ''
        if company_data['Вид деятельности']:
            for info in company_data['Вид деятельности']:
                content += f'{info}, '
            ws1[f'E{row}'] = content
            row += 1

    wb.save(filename=file_name)
    print(Fore.GREEN + f'\nОбработка завершена. Сохранен файл {file_name}.')


