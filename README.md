# ruina-wiki-repository
# 废都物语 Wiki

### 提交 pr 指南

本仓库使用了 mkdocs 框架，只需要在 docs 中的对应文件夹中，添加图片并且命名，然后在同一文件夹添加 md 文档。

然后在 mkdocs.yml 中，更改目录。

网站的原理是改好以上内容之后，在这个仓库中 mkdocs build 生成 site，然后将 site 中的文件复制到[网站仓库](https://github.com/Xenolies/xenolies.github.io)，即可更新。
