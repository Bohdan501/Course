import requests
import bs4
my_file = open("some.txt", "w",encoding='utf-8')

url = ""
start_url = 'http://quotes.toscrape.com'
while True:
    print(url)
    url = start_url + url
    responce = requests.get(url)
    soup = bs4.BeautifulSoup(responce.text, 'html.parser')
    for item in soup.find_all("div", {'class':'quote'}):
        aa=(item.span.text)
        bb=(item.find('small', {'class':'author'}).text)
        cc=aa+bb+'"'          

        my_file.write(cc+'\n')

    li = soup.find('li', {'class': 'next'})
    if li is None:
        break
    a = li.a
    url = a['href']
