#1. количество страниц
#2. сформировать список url
#3. собрать данные

#import requests #для получение ответа с сайта и сохранения текст html страницы
#from bs4 import BeautifulSoup #для парсинга полученного текста html страницы

import os
import requests
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Create_SQL_Shop import *
from bs4 import BeautifulSoup
import csv

def write_csv(data_list):
    with open('Toyo.csv','a') as f:
        writer = csv.writer(f)
        for k, v in data_list.items():
            for t, p in v.items():
                writer.writerow([k.strip(), t.strip(), p.strip()])

def sqllite_tab(data_list):
    engine = create_engine('sqlite:///shop.sqlite', echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create objects
    for k, v in data_list.items():
        for t,p in v.items():
            record= Shop(k,t,p)
            session.add(record)
        # commit the record the database
    session.commit()
    session.close()



def get_htm(url):
    r=requests.get(url,timeout=5)#Response [200] -не забанили
    return r.text#' <!DOCTYPE html><html itemscope itemtype="http://schema.org/WebPage" lang="ru-UA">

def get_pages(html):
    soup=BeautifulSoup(html,'lxml')
    pages=soup.find('div',class_='category tyrebrand').find_all('a', class_='item model-item')
    # title, item-lower
    base_url = 'https://shinoman.ua'
    data={}
    for ad in pages:
        try:
            category=ad.find('span',class_='item-title').get('title')#получили название категории
        except:
            category = ''
        try:
            title=ad.find('span',class_='item-title').text#получили текст названия
        except:
            title = ''
        try:
            price=ad.find('span', class_='item-lower').text#получили текст цены
        except:
            price=''
        #это нужно вынести в отдельную функцию
        # try:
        #     url_img =base_url+ad.find('img').get('src')
        #     p = requests.get(url_img)
        #     out = open(category.strip()+title.strip()+'.jpg', 'bw')
        #     out.write(p.content)
        #     out.close()
        # except:
        #     url_img=''


            #https: // shinoman.ua / images / pic / thumbs600 / mini_2136.jpg

        data.setdefault(category, {title: price})



    sqllite_tab(data)
    write_csv(data)

   # .get('href')#'/toyo/tranpath-mpz.html'
   # return pages
   # pages = soup.find('div', class_='brand-season').find_all('a', class_='item model-item')[-1].get('href')
   # получили последний элемент и в нем может содержаться номер страницы
   # total_pages=pages.split('=')[1].split('&')[0] #делим строку по символу равно, после равно получаем номер страницы(проверить код на сайте)
   # второй элемент содержит номер страницы именно на этом сайте, второй элемент делим и получаем первый
   # return int(total_pages) # вернули номер последней страницы
   #

def main():
    url='https://shinoman.ua/toyo.html'
    #разбиваем адрес на части
    # base_url='https://shinoman.ua/'
    # part_url='toyo'
    #end_url='.html'
    total_pages=get_pages(get_htm(url))


if __name__=='__main__':
    main()
