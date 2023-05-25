'''
将指定的文本/数据转换为epub格式
'''

from ebooklib import epub
import json


def create_epub(original_data_path, epub_path, epub_title):
    '''

    :param original_data_path: 数据所在的路径
    :param epub_path: epub文件所在的路径
    :param epub_title: epub文件标题
    :return:
    '''
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
    book.set_cover('cover.jpg', open('../static/cover-5.jpg', 'rb').read())

    # 生成epub文件
    epub.write_epub(epub_path, book, {})


if __name__ == '__main__':
    create_epub("../data/json/tpo-51-54.json", "../data/epub/TOEFL TPO 51~54.epub",
                "TOEFL TPO 51~54")
