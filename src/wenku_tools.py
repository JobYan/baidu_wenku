#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
 * @Author       : JobYan
 * @Email        : jobyan@foxmail.com
 * @Date         : 2022-11-25 15:15:51
 * @LastEditors  : JobYan
 * @LastEditTime : 2022-11-26 14:38:32
 * @FilePath     : \wenku_tools.py
 * @Description  : 下载PPT的免费部分保存为图片，并将这些图片合并为pdf
"""
import os
import re
import urllib
import datetime

import fitz
import requests
from bs4 import BeautifulSoup


# 下载html
def download(url, user_agent="wswp", num_retries=2):
    # print("Downloading: ", url)
    headers = {"User-agent": user_agent}
    request = urllib.request.Request(url, headers=headers)
    try:
        html = urllib.request.urlopen(request)
        # print(html.read().decode("utf-8"))
    except urllib.error.URLError as e:
        # print("Download error: ", e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code <= 600:
                # 如果是5xx错误，则进行重试
                return download(url, user_agent, num_retries - 1)
    return html


class wenku():
    def __init__(self):
        self.image_path_list = []
        self.link_list = []
        self.title = ''
        self.type = ''
        self.dir = ''
        self.image_dir = ''
        self.html_content = None
        self.cookie = None
        self.user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
        self.header = {'User-Agent': self.user_agent}

    def get_cookie(self):
        res = requests.get('https://wenku.baidu.com', headers=self.header)
        self.cookie = res.cookies

    # 批量下载图片
    def download_imgs(self, url_list, dir):
        url_num = len(url_list)
        for i in range(url_num):
            image_path = os.path.join(dir, f'{i}.png')
            content = download(url_list[i], self.user_agent)
            with open(image_path, 'wb') as f:
                f.write(content.read())  # 将内容写入图片
                f.close()
            self.image_path_list.append(image_path)

    # 解析pdf网页的图片链接
    def parse_links(self, html_content):
        img_links = []
        if self.type == "pdf":
            links = re.findall("\"png\"\:\[(.*?)\]", html_content.decode('utf-8'))
            if links:
                self.link_list = re.findall("\"pageIndex\"\:\d+\,\"pageLoadUrl\"\:\"(.*?)\"\}", links[0])
        elif self.type == "ppt":
            soup = BeautifulSoup(html_content, 'html.parser')
            img_srcs = soup.find_all('img')
            for img_src in img_srcs:
                img_link = img_src.get('src')
                if img_link:
                    self.link_list.append(img_link)
                else:
                    self.link_list.append(img_src.get('data-src'))

    def export_pdf(self, dir, pdf_name, img_paths):
        doc = fitz.open()
        for img_path in img_paths:
            imgdoc = fitz.open(img_path)  # 打开图片
            pdfbytes = imgdoc.convert_to_pdf()  # 使用图片创建单页的 PDF
            imgpdf = fitz.open("pdf", pdfbytes)
            doc.insert_pdf(imgpdf)  # 将当前页插入文档

        # 保存在图片文件夹下
        save_pdf_path = os.path.join(dir, pdf_name)
        if os.path.exists(save_pdf_path):
            os.remove(save_pdf_path)

        doc.save(save_pdf_path)  # 保存pdf文件
        doc.close()

    def create_dir(self):
        if not os.path.exists(self.dir):
            os.makedirs(self.dir)
        if not os.path.exists(self.image_dir):
            os.makedirs(self.image_dir)

    def process(self, url):
        # if not url:
        #     print("URL为空")
        self.link_list = []
        self.image_path_list = []
        self.get_cookie()  # 获取cookie
        self.html_content = requests.get(url, headers=self.header, cookies=self.cookie).content
        self.title = re.findall("\"title\":\"(.*?)\"", self.html_content.decode('utf-8'))[-1]
        self.type = re.findall("\"fileType\"\:\"(.*?)\"", self.html_content.decode('utf-8'))[0]
        time_str = datetime.datetime.now().strftime('_%H_%M_%S')
        self.dir = os.path.join(self.dir, self.title + time_str)
        self.image_dir = os.path.join(self.dir, "images")

        self.create_dir()
        self.parse_links(self.html_content)

        self.download_imgs(self.link_list, self.image_dir)
        self.export_pdf(self.dir, self.title + '.pdf', self.image_path_list)


if __name__ == "__main__":
    user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
    header = {
        'User-Agent': user_agent}
    res = requests.get('https://wenku.baidu.com', headers=header)
    cookie = res.cookies

    url = "https://wenku.baidu.com/view/e966626f7cd184254b3535d7"  # PDF
    url = "https://wenku.baidu.com/view/ce7b269b72fe910ef12d2af90242a8956becaa7c.html"
    url = "https://wenku.baidu.com/view/8b4702b38762caaedc33d400?aggId=ce7b269b72fe910ef12d2af90242a8956becaa7c&fr=catalogMain&_wkts_=1670763996834"

    wk = wenku()
    wk.process(url)
