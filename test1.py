# # coding:utf-8
# import requests
# from bs4 import BeautifulSoup
# import re
#
#
# def get_urls(mulu_url):
#     a = requests.get(mulu_url).content
#     b = a.decode('utf-8')
#     soup = BeautifulSoup(b, features="html.parser")
#     c = soup.select('.dccss')
#     urls = []
#     for i in range(len(c) - 3):
#         url = "https://www.lewengu.com" + c[i].a['href']
#         urls.append(url)
#     return urls
#
#
# #   利用BeautifulSoup进行筛选
# def download_book(mulu_url):
#     urls1 = get_urls(mulu_url)
#     for url1 in urls1:
#         a1 = requests.get(url1).content
#         b1 = a1.decode('utf-8')
#         soup1 = BeautifulSoup(b1, features="html.parser")
#         d = soup1.find_all('h2')[0].text
#         title = soup1.find_all('h1')[0].text
#         c1 = soup1.find_all('p')[0].text
#         section_text = re.sub('\s+', '\r\n\t', c1).strip('\r\n')
#         book_name = d + '.txt'
#         fp = open(book_name, 'a', encoding='utf-8')
#         fp.write(title + "\n")
#         fp.write(section_text + "\n")
#         print(title + '---已下载')
#
#
# download_book('http://www.lewengu.com/books/65/65995/')


import re
import requests
from bs4 import BeautifulSoup


def get_urls(mulu_url):
    a = requests.get(mulu_url).content
    b = a.decode('utf-8')
    soup = BeautifulSoup(b, features="html.parser")
    c = soup.select('.dccss')
    urls = []
    for i in range(len(c) - 3):
        url = "https://www.lewengu.com" + c[i].a['href']
        urls.append(url)
    return urls


#   利用正则表达式进行筛选
urls1 = get_urls("https://www.lewengu.com/books/65/65995/")
for url1 in urls1:
    a = requests.get(url1).content
    a = a.decode("utf-8")
    reg1 = r'<H1>(.*?)</H1>'
    reg1 = re.compile(reg1)
    chapter_title = re.findall(reg1, a)[0]
    reg3 = r'<H2>(.*?)</H2>'
    reg3 = re.compile(reg3)
    book_title = re.findall(reg3, a)[0]
    reg2 = r'<P>(.*?)</P>'
    reg2 = re.compile(reg2)
    chapter_content = re.findall(reg2, a)[0]
    content = chapter_content.replace("&nbsp;&nbsp;&nbsp;&nbsp;", "\t")
    content = content.replace("<br /><br />", "\r\n")
    book = book_title + '.txt'
    f = open(book, 'a', encoding='utf-8')
    f.write(chapter_title + "\r\n")
    f.write(content + "\r\n")
    print(chapter_title + '---已下载')



