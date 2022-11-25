
import re


# Задача № 1
# s = '31'
# reg = r'(?:0?[1-9]|[12][0-9]|[3][01])'

# s = '12'
# reg = r'(?:0?[1-9]|[1][12])'

# s = '2022'
# reg = '([1][9][0-9][0-9]|[2][0][0-2][0-9])'

# data = "30-12-2023"
# reg = r'^(?:0?[1-9]|[12][0-9]|[3][01])[-](?:0?[1-9]|[1][12])[-]([1][9][0-9][0-9]|[2][0][0-2][0-9]$)'
# print(re.findall(reg, data))
# reg1 = r'[^\d]'
# data1 = ' '.join(re.split(reg1, data))
# print(data1)
# reg2 = r'(\d{2}[ ])(\d{2}[ ])(\d{4})'
# print(re.findall(reg2, data1))


def data(s):
    reg = r'^(?:0?[1-9]|[12][0-9]|[3][01])[-](?:0?[1-9]|[1][12])[-]([1][9][0-9][0-9]|[2][0][0-2][0-9]$)'
    reg1 = r'[^\d]'
    reg2 = r'(\d{2}[ ])(\d{2}[ ])(\d{4})'

    if re.findall(reg, s) == []:
        print('Неправильно осуществлён ввод данных')
    else:
        print('Результат: ', re.findall(reg2, ' '.join(re.split(reg1, s))))


d_m_year = input('Введите дату, месяц, год в формате dd-mm-yyyy: ')
data(d_m_year)


#  Задача № 2

# s1 = '+7 499-456-45-78'
# s2 = '+74994564578'
# s3 = '7 (499) 456 45 78'
# s4 = '+7 (499) 456-45-78'
# reg = r'^([+]*\d{1}[\s|(]*\d{3}[)|\s|-]*\d{3}[\s|-]*\d{2}[\s|-]*\d{2})$'
# print(re.findall(reg, s1))
# print(re.findall(reg, s2))
# print(re.findall(reg, s3))
# print(re.findall(reg, s4))


# ДЗ № 22-1
test = "1X, Text, ACC 123 A1B2C3"
reg4 = r'(\D|\d{3})'

# print(re.findall(reg4, test))
# print(re.sub(reg4, r'', test))
st = re.sub(reg4, r'', test)
s = list(st)
print(s)
print(list(re.sub(reg4, r'', test)))


# ДЗ №22-2
# txt1 = "#START# tile #END#"
# reg = r'[a-z]{4}'
# print(re.findall(reg, txt1))
#
# reg2 = r'#[A-Z]+#'
# print(re.sub(reg2, r'', txt1))

# ДЗ № 22-3
# dig = "12_34__56"
# reg = r'\A\d{2}'
# print(re.findall(reg, dig))