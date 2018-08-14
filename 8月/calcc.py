from bs4 import BeautifulSoup
import requests

class Crawler:

    def __init__(self,url):
        self._url = url
        self.soup = BeautifulSoup(self.get_webpage(self.url))

    
    def get_webpage(self,url):   
        return requests.get(url).content

    def get_title(self, className):
        soup.find_all('div', class=className)
        return 

    def get_description(self, className):
        soup.find_all('div', class=className)

    def get_container(self, clasName):
        soup.find_all('div', className=className)

if __name__ == '__main__':
    crawler = Crawler("https://shopee.tw/%E7%BE%85%E5%87%A1%E8%BF%AA%E8%A9%A9-ROVENDIS-%E6%8E%A7%E6%B2%B9%E6%B4%97%E9%AB%AE%E7%B2%BE-i.18662668.194116229")