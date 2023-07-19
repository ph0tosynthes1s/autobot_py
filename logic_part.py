import asyncio
import sys
import json
import requests
import re



import xml.etree.ElementTree as ET
import urllib.request
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from db import Database

from arsenic import get_session, keys, browsers, services

from requests_html import AsyncHTMLSession


db = Database('database.db')

#общий подсчет
async def calculate_full(year, volume, after_price):
    price = float(after_price)
    year_pattern = re.compile(r'\w+')
    year_word = year_pattern.findall(year)[0]
    get_volume = float(volume)
    if year_word == 'До':
        volume_price = after_price * 24/100

    elif year_word == 'От':
        if get_volume< 1000:
            volume_price = get_volume*1.5/2
        elif get_volume>=1001 and get_volume<=1500:
            volume_price = get_volume*1.7/2
        elif get_volume>=1501 and get_volume<=1800:
            volume_price = get_volume*2.5/2
        elif get_volume>=1801 and get_volume<=2300:
            volume_price = get_volume*2.7/2
        elif get_volume>=2301 and get_volume<=3000:
            volume_price = get_volume*3/2
        elif get_volume>=3001:
            volume_price = get_volume*3.6/2


    elif year_word == 'Более':
        if get_volume < 1000:
            volume_price = get_volume*3/2
        elif get_volume>=1001 and get_volume<=1500:
            volume_price = get_volume*3.2/2
        elif get_volume>=1501 and get_volume<=1800:
            volume_price = get_volume*3.5/2
        elif get_volume>=1801 and get_volume<=2300:
            volume_price = get_volume*4.8/2
        elif get_volume>=2301 and get_volume<=3000:
            volume_price = get_volume*5/2
        elif get_volume>=3001:
            volume_price = get_volume*5.7/2
    return volume_price

async def calculate_full_electro(year, after_price):
    price = float(after_price)
    year_pattern = re.compile(r'\w+')
    year_word = year_pattern.findall(year)[0]
    if year_word == 'До':
        volume_price = after_price * 7.5/100

    elif year_word == 'От':
        volume_price = after_price * 7.5/100


    elif year_word == 'Более':
        volume_price = after_price * 7.5/100

    return volume_price

async def calculate_full_comercial(year, price_rubls):
    year_pattern = re.compile(r'\w+')
    year_word = year_pattern.findall(year)[0]
    if year_word == 'До':
        volume_price = price_rubls + 850000

    elif year_word == 'Старше':
        volume_price = price_rubls + 3500000
    return volume_price

async def calculate_full_moto(year, volume, after_price):
    price = float(after_price)
    year_pattern = re.compile(r'\w+')
    year_word = year_pattern.findall(year)[0]
    get_volume = float(volume)
    if year_word == 'До':
        if get_volume <= 799:
            volume_price = after_price * 37/100
        elif get_volume >=800:
            volume_price = after_price * 32/100


    elif year_word == 'От':
        if get_volume <= 799:
            volume_price = after_price * 37/100
        elif get_volume >=800:
            volume_price = after_price * 32/100


    elif year_word == 'Более':
        if get_volume <= 799:
            volume_price = after_price * 37/100
        elif get_volume >=800:
            volume_price = after_price * 32/100

    return volume_price


#перевод евро в рубль
async  def get_rubls(price):
    url = ("https://iss.moex.com/iss/engines/currency/markets/selt/boards/CETS/securities/EUR_RUB__TOM.jsonp")
    data = requests.get(url)
    text = data.text
    text = re.sub(r'\n', "", text)
    json_string = json.loads(text)
    value = json_string['marketdata']['data'][0][8]
    result = price * float(value)
    return result

#перевод рубля в евро
async  def get_euro(price):
    url = ("https://iss.moex.com/iss/engines/currency/markets/selt/boards/CETS/securities/EUR_RUB__TOM.jsonp")
    data = requests.get(url)
    text = data.text
    text = re.sub(r'\n', "", text)
    json_string = json.loads(text)
    value = json_string['marketdata']['data'][0][8]
    print(value)
    result = int(price)/round(int(value))
    return result


#подсчет нетто
async def calculate_netto(price, year, volume, pts):
    get_price = float(price)
    fitst_price = (get_price + get_price/100*7)
    after_price = float(fitst_price) + ((get_price + get_price/100*7)/100*3)
    price_euro = after_price + await calculate_full(year, volume, after_price)
    final_price_euro = float(price_euro) + 3800
    price_rubls = await get_rubls(final_price_euro)
    if pts == 'С кнопкой ГЛОНАСС':
        price_rubls_pts = float(price_rubls) + 125000
    else:
        price_rubls_pts = float(price_rubls) + 68000
    float_price_rubls = price_rubls_pts/100*8.5
    final_price_rubls = float(price_rubls_pts) + float(float_price_rubls)
    return final_price_rubls


#подсчет брутто
async def calculate_brutto(price, year, volume, pts):
    get_price = float(price)
    fitst_price = (get_price + get_price/100*5)
    after_price = float(fitst_price) + ((get_price + get_price/100*5)/100*3)
    price_euro = after_price + await calculate_full(year, volume, after_price)
    final_price_euro = float(price_euro) + 3800
    price_rubls = await get_rubls(final_price_euro)
    if pts == 'С кнопкой ГЛОНАСС':
        price_rubls_pts = float(price_rubls) + 125000
    else:
        price_rubls_pts = float(price_rubls) + 68000
    float_price_rubls = price_rubls_pts/100*8.5
    final_price_rubls = float(price_rubls_pts) + float(float_price_rubls)
    return final_price_rubls

#обработка ссылки
async def get_link_ru(link):
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36"
    }
    url = f'{link}'
    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    nameParsed  = soup.find("h1", {"class": "g-col-8"}).contents
    priceSecondCheck = soup.find("p", {"class": "h3"}).find_next_sibling("p")
    priceParsed = None
    priceSecondParsed = None
    if not (priceSecondCheck is None):
        priceSecondParsed  = soup.find("p", {"class": "h3"}).find_next_sibling("p").contents
        priceParsed = soup.find("p", {"class": "h3"}).contents
    else:
        priceParsed = soup.find("p", {"class": "h3"}).contents
    cubesCheck  = soup.find('span', string = "Объем двигателя")
    if not (cubesCheck is None):
        cubesParsed = soup.find('span', string="Объем двигателя").parent.find("span", {"class": "u-text-bold"}).contents
        cubesReplaced = re.findall(r"\d+", cubesParsed[0])
        if len(cubesReplaced) > 1:
            cubesGet = str(cubesReplaced[0]) + str(cubesReplaced[1])
        else:
            cubesGet = str(cubesReplaced[0])
        cubes = cubesGet
    else:
        cubes= 0
    dateCheck = soup.find('span', string = "Первая регистрация")
    if not (dateCheck is None):
        dateParsed = soup.find('span', string = "Первая регистрация").parent.find("span", {"class": "u-text-bold"}).contents
        year = ""
        date = dateParsed[0]
        for i in range(len(date) - 3):
            num = True
            for j in range(4):
                num = num & date[i + j].isdigit()
            if num:
                year = ""
                for j in range(4):
                    year += date[i + j]
        age = 2023 - int(year)
        age_final = ""
        if age < 3:
            age_final = 'До 3 лет'
        elif age >=3 and age <= 5:
            age_final = 'От 3 до 5 лет'
        elif age > 5:
            age_final = 'Более 5 лет'
    else:
        date = 'Не регестрировался'
        age_final = 'До 3 лет'
    name = nameParsed[0]
    priceReplaced = priceParsed[0].replace(u'\xa0', u'')
    priceGet = re.findall(r"\d+", priceReplaced)
    price = int(priceGet[0])
    if (priceSecondParsed is None):
        full_data = {
            'price' : int(price),
            'priceNull': 1,
            'volume': int(cubes),
            'age': str(age_final),
            'name': str(name),
            'first': str(date)
        }
        dump = json.dumps(full_data, ensure_ascii=False)
        load = json.loads(dump)
    else:
        priceReplaced = priceParsed[0].replace(u'\xa0', u'')
        priceGet = re.findall(r"\d+", priceReplaced)
        price = int(priceGet[0])
        priceSecondReplaced = priceSecondParsed[0].replace(u'\xa0', u'')
        priceSecondGet = re.findall(r"\d+", priceSecondReplaced)
        priceSecond = int(priceSecondGet[0])
        full_data = {
            'price': int(priceSecond),
            'priceNull' : 0,
            'volume': int(cubes),
            'age': str(age_final),
            'name': str(name),
            'first': str(date)
        }
        dump = json.dumps(full_data, ensure_ascii=False)
        load = json.loads(dump)
    return load

async def get_link_ru_electro(link):
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36"
    }
    url = f'{link}'
    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    nameParsed  = soup.find("h1", {"class": "g-col-8"}).contents
    priceSecondCheck = soup.find("p", {"class": "h3"}).find_next_sibling("p")
    priceParsed = None
    priceSecondParsed = None
    if not (priceSecondCheck is None):
        priceSecondParsed  = soup.find("p", {"class": "h3"}).find_next_sibling("p").contents
        priceParsed = soup.find("p", {"class": "h3"}).contents
    else:
        priceParsed = soup.find("p", {"class": "h3"}).contents
    dateCheck = soup.find('span', string="Первая регистрация")
    if not (dateCheck is None):
        dateParsed = soup.find('span', string="Первая регистрация").parent.find("span",
                                                                                {"class": "u-text-bold"}).contents
        year = ""
        date = dateParsed[0]
        for i in range(len(date) - 3):
            num = True
            for j in range(4):
                num = num & date[i + j].isdigit()
            if num:
                year = ""
                for j in range(4):
                    year += date[i + j]
        age = 2023 - int(year)
        age_final = ""
        if age < 3:
            age_final = 'До 3 лет'
        elif age >= 3 and age <= 5:
            age_final = 'От 3 до 5 лет'
        elif age > 5:
            age_final = 'Более 5 лет'
    else:
        date = 'Не регестрировался'
        age_final = 'До 3 лет'
    name = nameParsed[0]
    priceReplaced = priceParsed[0].replace(u'\xa0', u'')
    priceGet = re.findall(r"\d+", priceReplaced)
    price = int(priceGet[0])
    if (priceSecondParsed is None):
        full_data = {
            'price' : int(price),
            'priceNull': 1,
            'age': str(age_final),
            'name': str(name),
            'first': str(date)
        }
        dump = json.dumps(full_data, ensure_ascii=False)
        load = json.loads(dump)
    else:
        priceReplaced = priceParsed[0].replace(u'\xa0', u'')
        priceGet = re.findall(r"\d+", priceReplaced)
        price = int(priceGet[0])
        priceSecondReplaced = priceSecondParsed[0].replace(u'\xa0', u'')
        priceSecondGet = re.findall(r"\d+", priceSecondReplaced)
        priceSecond = int(priceSecondGet[0])
        full_data = {
            'price': int(priceSecond),
            'priceNull' : 0,
            'age': str(age_final),
            'name': str(name),
            'first': str(date)
        }
        dump = json.dumps(full_data, ensure_ascii=False)
        load = json.loads(dump)
    return load

async def get_link_ru_comercial(link):
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36"
    }
    url = f'{link}'
    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    nameParsed  = soup.find("h1", {"class": "g-col-8"}).contents
    priceSecondCheck = soup.find("p", {"class": "h3"}).find_next_sibling("p")
    priceParsed = None
    priceSecondParsed = None
    if not (priceSecondCheck is None):
        priceSecondParsed  = soup.find("p", {"class": "h3"}).find_next_sibling("p").contents
        priceParsed = soup.find("p", {"class": "h3"}).contents
    else:
        priceParsed = soup.find("p", {"class": "h3"}).contents
    dateCheck = soup.find('span', string="Первая регистрация")
    if not (dateCheck is None):
        dateParsed = soup.find('span', string="Первая регистрация").parent.find("span",
                                                                                {"class": "u-text-bold"}).contents
        year = ""
        date = dateParsed[0]
        for i in range(len(date) - 3):
            num = True
            for j in range(4):
                num = num & date[i + j].isdigit()
            if num:
                year = ""
                for j in range(4):
                    year += date[i + j]
        age = 2023 - int(year)
        age_final = ""
        if age < 3:
            age_final = 'До 3 лет'
        elif age >= 3:
            age_final = 'Старше 3 лет'
    else:
        date = 'Не регестрировался'
        age_final = 'До 3 лет'
    name = nameParsed[0]
    priceReplaced = priceParsed[0].replace(u'\xa0', u'')
    priceGet = re.findall(r"\d+", priceReplaced)
    price = int(priceGet[0])
    if (priceSecondParsed is None):
        full_data = {
            'price' : int(price),
            'priceNull': 1,
            'age': str(age_final),
            'name': str(name),
            'first': str(date)
        }
        dump = json.dumps(full_data, ensure_ascii=False)
        load = json.loads(dump)
    else:
        priceReplaced = priceParsed[0].replace(u'\xa0', u'')
        priceGet = re.findall(r"\d+", priceReplaced)
        price = int(priceGet[0])
        priceSecondReplaced = priceSecondParsed[0].replace(u'\xa0', u'')
        priceSecondGet = re.findall(r"\d+", priceSecondReplaced)
        priceSecond = int(priceSecondGet[0])
        full_data = {
            'price': int(priceSecond),
            'priceNull' : 0,
            'age': str(age_final),
            'name': str(name),
            'first': str(date)
        }
        dump = json.dumps(full_data, ensure_ascii=False)
        load = json.loads(dump)
    return load

async def get_link(link):
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36"
    }
    url = f'{link}'
    r = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(r.text, 'html.parser')
    nameParsed  = soup.find("h1", {"class": "h2"}).contents
    subtitleParsed  = soup.find("div", {"class": "listing-subtitle"}).contents
    priceSecondCheck = soup.find("div", {"id": "main-cta-box-price-row"}).find("span", {"class": "u-margin-top-9"})
    priceParsed = None
    priceSecondParsed = None
    if not (priceSecondCheck is None):
        priceSecondParsed  = soup.find("span", {"class": "u-margin-top-9"}).find_previous_sibling('span').contents
        priceParsed = soup.find("span", {"class": "h3"}).contents
    else:
        priceParsed = soup.find("span", {"class": "h3"}).contents
    cubesCheck  = soup.find("div", {"id": "cubicCapacity-v"})
    if not (cubesCheck is None):
        cubesParsed  = soup.find("div", {"id": "cubicCapacity-v"}).contents
        if '.' in cubesParsed[0]:
            cubesReplaced = re.findall("\d+\.\d+", cubesParsed[0])
            cubesGet = cubesReplaced[0].replace(".", "")
        else:
            cubesReplaced = re.findall("\d+", cubesParsed[0])
            cubesGet = cubesReplaced[0]
        cubes = cubesGet
    else:
        cubes= 0
    dateCheck = soup.find("div", {"id": "firstRegistration-v"})
    if not (dateCheck is None):
        dateParsed = soup.find("div", {"id": "firstRegistration-v"}).contents
        year = ""
        date = dateParsed[0]
        for i in range(len(date) - 3):
            num = True
            for j in range(4):
                num = num & date[i + j].isdigit()
            if num:
                year = ""
                for j in range(4):
                    year += date[i + j]
        age = 2023 - int(year)
        age_final = ""
        if age < 3:
            age_final = 'До 3 лет'
        elif age >=3 and age <= 5:
            age_final = 'От 3 до 5 лет'
        elif age > 5:
            age_final = 'Более 5 лет'
    else:
        date = 'Не регестрировался'
        age_final = 'До 3 лет'
    priceReplaced = re.findall("\d+\.\d+", priceParsed[0])
    priceGet = priceReplaced[0].replace(".", "")
    price = priceGet
    name = nameParsed[0] + ' ' + subtitleParsed[0]
    if (priceSecondParsed is None):
        full_data = {
            'price' : int(price),
            'priceNull': 1,
            'volume': int(cubes),
            'age': str(age_final),
            'name': str(name),
            'first': str(date)
        }
        dump = json.dumps(full_data, ensure_ascii=False)
        load = json.loads(dump)
    else:
        priceSecondReplaced = re.findall("\d+\.\d+", priceSecondParsed[0])
        priceSecondGet = priceSecondReplaced[0].replace(".", "")
        priceSecond = priceSecondGet
        full_data = {
            'price': int(priceSecond),
            'priceNull' : 0,
            'volume': int(cubes),
            'age': str(age_final),
            'name': str(name),
            'first': str(date)
        }
        dump = json.dumps(full_data, ensure_ascii=False)
        load = json.loads(dump)
    return load




