import requests
datas = requests.get("https://www.jumia.com.ng/")
from bs4 import BeautifulSoup
# print(datas.content)
feed = datas.content
feed_content = BeautifulSoup(feed, "html.parser")
feed_prett = feed_content.prettify()
contents = feed_content.findAll("img")
