'''
Author: ddy-ddy
Date: 2023-05-24 14:00:52
LastEditTime: 2023-05-24 21:14:20
Github: https://github.com/ddy-ddy
Website: https://ddy-ddy.com
'''
from ebooklib import epub
import json


def create_epub(original_data_path, epub_path, epub_title):
    # 读取json数据
    with open(original_data_path, 'r') as f:
        data = json.load(f)

    # 创建epub文件
    book = epub.EpubBook()
    book.set_title(epub_title)
    book.set_language('en')
    book.add_author('ddy')

    # 添加字体样式
    style = 'body { font-family: Times, Times New Roman, serif; }'
    nav_css = epub.EpubItem(uid="style_nav",
                            file_name="style/nav.css",
                            media_type="text/css",
                            content=style)
    book.add_item(nav_css)

    # 遍历json数据，添加章节
    chapterList = []
    for item in data:
        chapter = epub.EpubHtml(title=item['id'],
                                file_name=item['id'] + '.xhtml',
                                lang="en")
        chapter.content = '<h1>' + item['title'] + '</h1>' + "<p>" + '<br>'.join(item['article']) + "</p>"
        book.add_item(chapter)
        chapterList.append(chapter)

    # 添加目录
    book.toc = chapterList
    book.spine = chapterList
    book.add_item(epub.EpubNcx())

    # 设置封面
    book.set_cover('cover.jpg', open('../static/cover-1.jpg', 'rb').read())

    # 生成epub文件
    epub.write_epub(epub_path, book, {})


if __name__ == '__main__':
    create_epub("../data/json/tpo-30-35.json", "../data/epub/TOEFL TPO 30~35.epub",
                "TOEFL TPO 30~35")
