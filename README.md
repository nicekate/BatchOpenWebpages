# BatchOpenWebpages.py

This Python script is used to open search result pages on Twitter, YouTube, and Xiaohongshu in bulk.

## Usage

1. Add the keywords you want to search for in the `query.txt` file, one keyword per line.
2. Run the `BatchOpenWebpages.py` script.

## How It Works

The script reads each line in the `query.txt` file, URL encodes the content of each line, generates the corresponding search URLs for Twitter, YouTube, and Xiaohongshu, and then opens these URLs in the default browser.

## Notes

- Make sure your system has Python and the necessary libraries (such as `webbrowser` and `urllib`) installed.
- Make sure the `query.txt` file and the `BatchOpenWebpages.py` script are in the same directory.
- If your system's default browser is not the browser you want to use, you may need to change your system's default browser settings.

---

# BatchOpenWebpages.py 中文说明

这个Python脚本用于批量打开Twitter、YouTube和小红书上的搜索结果页面。

## 使用方法

1. 在`query.txt`文件中添加你想要搜索的关键词，每行一个关键词。
2. 运行`BatchOpenWebpages.py`脚本。

## 工作原理

该脚本读取`query.txt`文件中的每一行，对每行内容进行URL编码，生成相应的Twitter、YouTube和小红书的搜索URL，然后在默认浏览器中打开这些URL。

## 注意事项

- 确保你的系统已安装Python及所需库（如`webbrowser`和`urllib`）。
- 确保`query.txt`文件和`BatchOpenWebpages.py`脚本位于同一目录下。
- 如果你的系统默认浏览器不是你想要使用的浏览器，你可能需要更改系统的默认浏览器设置。