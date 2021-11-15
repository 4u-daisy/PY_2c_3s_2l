import json
import re
from tqdm import tqdm
import argparse

class Validator:
    # summary
    # Класс Validator проверяющий корерктность данных
    # /summary
    def __init__(self):
        pass

    # summary
    # Инициализирует объект класса
    # /summary
    # pass - синтаксически требуется наличие какого-то оператора или выражения, но вам не нужно выполнение любых
    # действий.
    # Оператор pass является Null -операций – т. е. он возвращает Null , когда выполняется.

    # summary
    # Методы проверки валидности данных
    # /summary

    def check_email(email: str) -> bool:
        if re.match(r"^[^\s@]+@([^\s@.,]+\.)+[^\s@.,]{2,}$", email) is not None:
            return True
        return False

    def check_weight(height: float) -> bool:
        if re.match(r"1\.\d\d", str(height)) is not None:
            if 1.30 < float(height) < 2.20:
                return True
        return False

    def check_inn(inn: str) -> bool:
        if re.match(r"[\d]{12}", inn) is not None:
            return True
        return False

    def check_passport_series(passport_series: str) -> bool:
        if re.match(r"\d\d[ ]\d\d", str(passport_series)) is not None:
            return True
        return False

    def check_occupation(occupation: str) -> bool:
        if re.match(r"^[\D]+", occupation) is not None:
            return True
        return False

    def check_work_experience(work_experience: int) -> bool:
        if re.match(r"^\d+", str(work_experience)) is not None:
            if 0 < int(work_experience) < 100:
                return True
        return False

    def check_political_views(political_views: str) -> bool:
        if re.match(r"^\D+$", political_views) is not None:
            return True
        return False

    def check_worldview(worldview: str) -> bool:
        if re.match(r"^\D+$", worldview) is not None:
            return True
        return False

    def check_address(address: str) -> bool:
        if re.match(r"^ул\.\s[а-яА-Я.\s\d-]+\s+[0-9]+$", address) is not None:
            return True
        return False


parser = argparse.ArgumentParser()
parser.add_argument('input', help="Название файла, с которого считаываются данные")
parser.add_argument('output', help="Названия файла, куда сохранятся валидные данные")
args = parser.parse_args()

data = json.load(open(args.input, encoding='windows-1251'))

email = 0
height = 0
inn = 0
passport_series = 0
occupation = 0
work_experience = 0
political_views = 0
worldview = 0
address = 0

validate_data = list()
with tqdm(total=len(data)) as progressbar:
    for i in data:
        field = True
        if not Validator.check_email(i['email']):
            email += 1
            field = False
        if not Validator.check_weight(i['height']):
            height += 1
            field = False
        if not Validator.check_inn(i['inn']):
            inn += 1
            field = False
        if not Validator.check_passport_series(i['passport_series']):
            passport_series += 1
            field = False
        if not Validator.check_occupation(i['occupation']):
            occupation += 1
            field = False
        if not Validator.check_work_experience(i['work_experience']):
            work_experience += 1
            field = False
        if not Validator.check_political_views(i['political_views']):
            political_views += 1
            field = False
        if not Validator.check_worldview(i['worldview']):
            worldview += 1
            field = False
        if not Validator.check_address(i['address']):
            address += 1
            field = False
        if field:
            validate_data.append(i)
        progressbar.update(1)

output_file = open(args.output, 'w')
data_file = json.dumps(validate_data)
output_file.write(data_file)
output_file.close()

print("Количество валидных записей: ", len(validate_data))
print("Количество невалидных записей: ", len(data)-len(validate_data))
print(f'Количество невалидного email: {email}')
print(f'Количество невалидного роста: {height}')
print(f'Количество невалидного ИНН: {inn}')
print(f'Количество невалидных серий паспортов: {passport_series}')
print(f'Количество невалидного профессий: {occupation}')
print(f'Количество невалидного опыта работы: {work_experience}')
print(f'Количество невалидныъ политических взглядов: {political_views}')
print(f'Количество невалидного вероисповедания: {worldview}')
print(f'Количество невалидного адреса: {address}')