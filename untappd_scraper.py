import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_beer_data(beer_type):
    headers = {
        'authority': 'ssl.google-analytics.com',
        'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
        'accept-language': 'en-US,en;q=0.9',
        'referer': 'https://untappd.com/',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'image',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }

    response = requests.get(f'https://untappd.com/beer/top_rated?type={beer_type}',headers=headers,)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('div', class_= 'content')

    data = []

    for row in table.findAll('div', attrs = {'class':'beer-item'}):
        name = row.find('p', class_='name').text
        brewery = row.find('p', class_='style').text
        abv = row.find('p', class_='abv').text.strip()
        rating = row.find('span', class_='num').text
        number_of_ratings = row.find('p', class_='raters').text.strip()
        data.append({"name": name, "brewery": brewery, "abv": abv, "rating": rating, "number_of_ratings": number_of_ratings})

        print(data)
    # df = pd.DataFrame.from_dict(data)
    # print(df)
    

def get_styles():
    headers = {
        'authority': 'ssl.google-analytics.com',
        'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
        'accept-language': 'en-US,en;q=0.9',
        'referer': 'https://untappd.com/',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'image',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    }

    response = requests.get(f'https://untappd.com/beer/top_rated',headers=headers,)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('div', class_= 'content')

    for row in table.findAll('div', attrs = {'class':'filters'}):
        options = row.find_all('option')
        styles = [option.text.strip() for option in options]
        start_index = styles.index('Show All Countries')
        end_index = styles.index('Zimbabwe')
        del styles[start_index:end_index+1]
        styles.remove("Show All Styles")
        for x in styles[:]:
            if 'Historical' in x:
                styles.remove(x)

    new_lst = []
    for item in styles:
        new_item = item.replace(" ", "-")
        new_item = item.replace("/", "-")
        new_item = new_item.replace("-", " ")
        new_item = " ".join(new_item.split())
        new_item = new_item.replace(" ", "-")
        new_lst.append(new_item.lower())
        result = [s.split("(")[0] for s in new_lst]
    return result

x = get_styles()
# print(x)
for item in x:
    # print(item)
    get_beer_data(item)
