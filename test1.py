# coding:utf-8
import requests
from bs4 import BeautifulSoup
import re


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


def download_book(mulu_url):
    urls1 = get_urls(mulu_url)
    for url1 in urls1:
        a1 = requests.get(url1).content
        b1 = a1.decode('utf-8')
        soup1 = BeautifulSoup(b1, features="html.parser")
        d = soup1.find_all('h2')[0].text
        title = soup1.find_all('h1')[0].text
        c1 = soup1.find_all('p')[0].text
        section_text = re.sub('\s+', '\r\n\t', c1).strip('\r\n')
        book_name = d + '.txt'
        fp = open(book_name, 'a', encoding='utf-8')
        fp.write(title + "\n")
        fp.write(section_text + "\n")
        print(title + '---已下载')


download_book('http://www.lewengu.com/books/3/3454/')


# import re
# import urllib.request
#
#
# # 定义一个爬取网络小说的函数
# def getNovelContent():
#     html = urllib.request.urlopen("http://www.quanshuwang.com/book/44/44683").read()
#     html = html.decode("gbk")  # 转成该网址的格式
#     # <li><a href="http://www.quanshuwang.com/book/44/44683/15379609.html" title="引子 穿越的唐家三少，共2744字">引子 穿越的唐家三少</a></li>  #参考
#     reg = r'<li><a href="(.*?)" title=".*?">(.*?)</a></li>'  # 正则表达的匹配
#     reg = re.compile(reg)  # 可添加可不添加，增加效率
#     urls = re.findall(reg, html)
#     for url in urls:
#         print(url)
#         # chapter_url = url[0]  # 章节的超链接
#         # chapter_title = url[1]  # 章节的名字
#         # # print(chapter_title)
#         # chapter_html = urllib.request.urlopen(chapter_url).read()  # 正文内容源代码
#         # chapter_html = chapter_html.decode("gbk")
#         # chapter_reg = r'</script>&nbsp;&nbsp;&nbsp;&nbsp;.*?<br />(.*?)<script type="text/javascript">'
#         # chapter_reg = re.compile(chapter_reg, re.S)
#         # chapter_content = re.findall(chapter_reg, chapter_html)
#         # for content in chapter_content:
#         #     content = content.replace("&nbsp;&nbsp;&nbsp;&nbsp;", "")
#         #     content = content.replace("<br />", "")
#         #     # print(content)
#         #     f = open('{}.txt'.format(chapter_title), 'w')
#         #     f.write(content)
#
#
# getNovelContent()

