import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Union

def str_to_int(price: str) -> int:
    """Convert the string format of a number to an integer - if the string doesn't contain
    a number, returns 0"""
    return int(''.join(filter(str.isdigit, price))) if any(char.isdigit() for char in price) else 0

def scrape_items() -> List[Dict[str, Union[str, int]]]:
    """Get the response from the website, parse it, select all the items, for each item create a dictionary and append
    it to the items_list, returns the items_list"""
    # Applying the headers to the get request to get the regular website page and not the captcha
    response = requests.get('https://www.zap.co.il/deals/category/weeklysale',headers={
            'Accept-Language': 'en-US,en;q=0.9,he;q=0.8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
        })

    soup = BeautifulSoup(response.text, 'html.parser')
    items = soup.select('.SlideBox > a')

    items_list = []

    for item in items:
        item_dict = {
        'link': 'https://www.zap.co.il' + item['href'],
        'title': item.find(name='h3', class_='title').text,
        'price': str_to_int(item.find(name='div', class_='price').text),
        'delivery_cost': str_to_int(item.find(name='div', class_=['dealShipment', 'shipmentPrice']).text),
        'delivery_time': str_to_int(item.select_one('.dealSupplyPeriod > span').text),
        'image_url': item.select_one('.deal-image > img')['src']
        }
        items_list.append(item_dict)

    return items_list