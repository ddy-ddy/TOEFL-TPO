## TOEFL-TPO

- 该仓库收集了托福`tpo 30~54`的阅读真题
- 阅读的原始数据保存在`data/json`文件夹中，可供任意操作
- 阅读的epub格式保存在`data/epub`文件夹中，可导入到阅读编辑器中

## JSON数据格式
- 原始数据存储为json格式，每个字典代表一篇文章
- 每篇文章的每个段落保存在`article`字段中
```json
[
  {
    "id": "tpo-30-1",                      //TPO30 第一篇阅读
    "title": "",                           //该篇文章标题
    "link": "",                            //考满分对应练习页面链接
    "article": [
      "A heated debate has enlivened...",  //该篇文章第一段
      "A heated debate has enlivened...",  //该篇文章第二段
      "A heated debate has enlivened..." 
    ]
  },
  {
    "id": "tpo-30-2", //TPO30 第二篇阅读
    "title": "",
    "link": "",
    "article": [
    ]
  },
  {
    "id": "tpo-30-3", //TPO30 第三篇阅读
    "title": "",
    "link": "",
    "article": [
    ]
  }
]
```
## epub数据格式
- epub格式的数据可以很方便的导入到各种电子表格中，方便大家的阅读
- 运行`src/text2epub.py`可以将指定的json数据转换为epub电子书的格式
<img src="https://ddy-1310349779.cos.ap-shanghai.myqcloud.com/typora/%E6%88%AA%E5%B1%8F2023-05-25%2017.57.59.jpg" style="zoom:50%;" />