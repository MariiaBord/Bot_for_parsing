# Парсер однопоточный
# Замер времени
# multiprocessing pool
# Замер времени
# Экспорт в csv

import requests #для получение ответа с сайта и сохранения текст html страницы
from bs4 import BeautifulSoup #для парсинга полученного текста html страницы

def get_html(url):
    r=requests.get(url, timeout=5)    #получение ответа от сервера по url адресу и установлено время ожидания
    return r.text          #объект класса Response библиотеки requests
                           # возвращет html код (только текст)

def get_all_links(html): #будет принимать html код страницы
    soup = BeautifulSoup(html,'lxml') #функция принимает 1й аргумент код-текст и 2й аргумент способ парсинга lxml

    #на сайте ищем таблицу 'table' с идентификатором curencies-all и id
    # нужно получить все ячейки. все td с классом currency-name. достаточно указать какое-то одно имя

    tds = soup.find('table',id='curencies-all').find('td', class_='currency-name')

    # tds - это список объектов soup, к которому применимы все методы объектов

    links=[] #список,  в котором будут спарсенные url

    for td in tds: #в td будет ссылка на объект soup
        #у каждого td есть тег a href
        a = td.find('a').get('href')# тут уже строка
        link='https://coinmarketcap.com'+a
        links.append(link)
    return links

def main():
    # берем главную страницу https://coinmarketcap.com/all/views/all
    #передаем ее функцию, получаем html код
    # и начинам ее парсить
    url='https://coinmarketcap.com/all/views/all'
    all_links= get_all_links(get_html(url))#список всех ссылок на каждую монету, передаем в эту переменную вызов функции

    for i in all_links:
        print(i)

if __name__=='__main__':
    main()

