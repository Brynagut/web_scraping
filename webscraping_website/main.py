from bs4 import BeautifulSoup
import requests
import time


class Request:
    def __init__(self):
        print('put som book that you are not familiar with')
        self.unfamiliar_book = input('>')



    def get_book(self):
        html_text = requests.get('http://books.toscrape.com/').text
        soup = BeautifulSoup(html_text, 'lxml')
        self.books = soup.find_all('li', class_ = 'col-xs-6 col-sm-4 col-md-3 col-lg-3')

        with open('C:\Harald\webscraping_website\posts\index.txt', 'a') as file:
            for index, book in enumerate(self.books):   
                price = book.find('div', class_ = 'product_price')
                title = book.find('h3').find('a').text
                price_c = price.find('p', class_ = 'price_color').text.replace('Â', '').replace('£', '')
                if float(price_c) > 50:
                    amount = "too expensive"
                else: 
                    amount = "good price"
        
                if self.unfamiliar_book not in title:
                        output = (f'''
                        Title: {title.strip()}
                        Price in pounds: {price_c.strip()}
                        Amount: {amount}
                        ''')
                        file.write(output)
                        file.write('\n\n')  # Add new lines between books

                print(f'book saved: {index}')



if __name__ == '__main__':
    while True:
        my_object = Request()
        my_object.get_book()
        time_wait = 10
        print(f'waiting {time_wait} minutes')
        time.sleep(time_wait * 60)
