import requests
import bs4
'''
    Basic Example
'''
# result = requests.get("http://www.example.com")

# print(result.text) # the html text
# soup = bs4.BeautifulSoup(result.text,"lxml")
# print(soup)

# print(soup.select('div')) # gives all the occurences of div (inclusive)
# print(soup.select('title')) # gives all the occurences of div (inclusive)
# print(soup.select('title')[0].getText()) ## get rid of the < >

'''
    Wikipedia
'''


# result = requests.get("https://en.wikipedia.org/wiki/Python_(programming_language)")
# soup = bs4.BeautifulSoup(result.text,"lxml")
#
# for i in soup.select('.toctext'): # all the table of contents
#     print(i.text)


'''
    Grabing an Image
'''

# soup = bs4.BeautifulSoup(requests.get("https://en.wikipedia.org/wiki/Python_(programming_language)").text,"lxml")
# res = soup.select(".thumbimage") # using the . because it is a class
#
# man = res[0] # the type of man is Tag which is a special type that is used as dictionary
#
# # print(man['src'])
# image_link = requests.get('https:'+man['src'])
# # print(image_link.content) # representing a binary view of the image
'''downloading image'''
# f = open('computer_image.jpg','wb')
# f.write(image_link.content)
# f.close()


'''
    toscrape.com
    get every book title with two stars 
'''

# base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
# #
# # star = '.star-rating'
# prod = '.product_pod'
# #
# # page = requests.get(base_url.format(1))
# # soup = bs4.BeautifulSoup(page.text,'lxml')
# TwoStar=[]
# # products = soup.select(prod)
# # print(products[0].select('.star-rating.Three')) # instead of SPACE use . -> star-rating.Two instead of star-rating Two
# for page_num in range(1,51):
#     page = requests.get(base_url.format(page_num))
#     page = bs4.BeautifulSoup(page.text,'lxml')
#     products = page.select(prod)
#     TwoStar.extend(list(map(lambda x: x.select('a')[1]['title'],filter(lambda x: len(x.select('.star-rating.Two'))!=0,products))))
#
#
# for i in TwoStar:
#     print(i)

'''
    Challenge
'''
# base_url = " http://quotes.toscrape.com/"
# page = bs4.BeautifulSoup(requests.get(base_url).text,'lxml')
#
# quotes_link = page.select('.quote')
# authors = set(map(lambda x: x.select('.author')[0].text,quotes_link))
# quotes = set(map(lambda x:x.select('.text')[0].text,quotes_link))
# tags = set(map(lambda x: x.text,page.select('.tag-item')))



