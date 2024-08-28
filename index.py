import requests
datas = requests.get("https://www.jumia.com.ng/")
from bs4 import BeautifulSoup
feed = datas.content
feed_content = BeautifulSoup(feed, "html.parser")
feed_prett = feed_content.prettify()
images = feed_content.findAll("img")
image_array = []
for image in images:
    # data_src = image.get("data-src")
    # if(data_src):
    #     image_array.append(data_src)
    #     print(image_array)

print(len(image_array))


# print(contents)


# print("hello")
