import re
import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession


session = HTMLSession()
soup = session.get("https://my.scheduling.com/selfscheduling/1.3.0/login")
soup.html.render()


print(soup.html.html)
