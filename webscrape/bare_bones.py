from bs4 import BeautifulSoup
import requests
url = 'http://www.prnewswire.com/news-releases/dutch-philosopher-koert-van-mensvoort-founder-of-the-next-nature-network-writes-a-letter-to-humanity-619925063.html'
r = requests.get(url)
html = r.text
soup = BeautifulSoup(html, 'lxml')