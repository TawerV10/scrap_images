from bs4 import BeautifulSoup
import requests

site = 'https://www.shopcwi.com/c-1061-dish-towels.aspx?pagesize=196'
response = requests.get(site)
soup = BeautifulSoup(response.text, 'lxml')

items = soup.find_all('div', class_='pimg')
print(len(items))

count = 1
for item in items:
    url = 'https://www.shopcwi.com/' + item.find('img').get('src')

    filename = url.split('/')[-1]
    with open(f'data/{filename}', 'wb') as f:
        response = requests.get(url)
        f.write(response.content)

        print(f'{count}.{url}')
        count += 1


