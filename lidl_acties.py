#by aahmetyildiz 2020

from lxml import html
from lxml import etree
import requests

#Url of page to crawl
url = "https://www.lidl.nl/acties"


#Get HTML code of URL and convert XML
source_code = requests.get(url)
html_text = html.fromstring(source_code.text)

#print(source_code.text)


#XPATHs
block_xpath = '//*[@class="product product--tile"]'
name_xpath = '//h3[@class="product__title"]/text()'
quantity_xpath = '//div[@class="pricebox__highlight"]/text()'
old_price_xpath = '//span[@class="pricebox__recommended-retail-price"]/text()'
new_price_xpath = '//span[@class="pricebox__price"]/text()'
date_xpath  = '//li[@class="ribbon__item ribbon__item--primary"]/div[@class="ribbon__text"]/text()'
description_xpath = '//li[@class="ribbon__item ribbon__item--danger"]/div[@class="ribbon__text"]/text()'


i = 0;

block_list = html_text.xpath(block_xpath)


#Crawl content for every block of product
for block in block_list:
    block_html_text = html.fromstring(etree.tostring(block))
    i+=1


    try:
        name = block_html_text.xpath(name_xpath)
        name = name[0].strip()
    except:
        name = ""

    try:
        quantity = block_html_text.xpath(quantity_xpath)
        quantity = quantity[0].strip()
    except:
        quantity = ""

    try:
        old_price = block_html_text.xpath(old_price_xpath)
        old_price = old_price[0].strip()
    except:
        old_price = ""

    try:
        new_price = block_html_text.xpath(new_price_xpath)
        new_price = new_price[0].strip()
    except:
        new_price = ""

    try:
        date = block_html_text.xpath(date_xpath)
        date = date[0].strip()
    except:
        date = ""

    try:
        description = block_html_text.xpath(description_xpath)
        description = description[0].strip()
    except:
        description = ""



    data = {
        'i': i,
        'name':name,
        'quantity': quantity,
        'old_price': old_price,
        'new_price': new_price,
        'date': date,
        'description': description,

    }


    print(data)
