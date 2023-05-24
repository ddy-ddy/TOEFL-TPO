'''
Author: ddy-ddy
Date: 2023-05-24 14:00:52
LastEditTime: 2023-05-24 14:25:22
Github: https://github.com/ddy-ddy
Website: https://ddy-ddy.com
'''
from ebooklib import epub
import json

# 读取json数据
with open('../json/tpo.json', 'r') as f:
    data = json.load(f)

# 创建epub文件
book = epub.EpubBook()
book.set_title('TOEFL TPO 30~35')
book.set_language('en')
book.add_author('ddy')

# 遍历json数据，添加章节
chapterList = []
for item in data:
    chapter = epub.EpubHtml(title=item['id'], file_name=item['id'] + '.xhtml', lang="en")
    chapter.content = '<h1>' + item['title'] + '</h1>' + '<br>'.join(item['article'])
    book.add_item(chapter)
    chapterList.append(chapter)

# # 添加目录
book.toc = chapterList
book.spine = chapterList
book.add_item(epub.EpubNcx())

# 设置封面
book.set_cover('cover.jpg', open('../static/cover.jpg', 'rb').read())

# 生成epub文件
epub.write_epub('../epub/TOEFL TPO 30~35.epub', book, {})
