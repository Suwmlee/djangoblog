介绍
----
一个基于 django 开发的 blog 程序，演示站点：[suwmlee.duapp.com][1]。特性包括：

  1. HTML5
  2. 友情链接
  3. 主题
  4. RSS
  5. Tinymce
  6. 内置评论系统
  7. SyntaxHighlighter

依赖
----

1. django >= 1.4
2. Tinymce

安装步骤
--------

1. 创建数据库，并在`setting.py`中设置好相关数据
2. 执行 `python manage.py syncdb` 同步数据库
3. 执行 `python manage.py runserver 0.0.0.0:8000` 启动临时服务器
4. 浏览器访问 `http://localhost:8000`，后台地址是 `http://localhost:8000/e/admin/`，口令在第 `2` 步时创建

[1]: http://suwmlee.duapp.com
