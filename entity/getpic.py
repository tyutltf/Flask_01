
from retrying import  retry
import requests
import urllib.request
import random
import json
import time


# 创建Img 类
class Img:
    def __init__(self,key):  # 初始化函数
        # 我们将要访问的url        {}是用于接受参数的     当前一次 json 数据 有30 条  ,
        self.temp_url = "http://image.so.com/zj?ch="+key
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36"
            , "Referer": "http://s.360.cn/0kee/a.html"
            , "Connection": "keep-alive"}
        self.num = 0

    def get_img_list(self, url):  # 获取 存放 图片url 的集合
        response = requests.get(url, headers=self.headers)
        html_str = response.content.decode()
        json_str = json.loads(html_str)
        img_str_list = json_str["list"]
        img_list = []
        for img_object in img_str_list:
            img_list.append(img_object["qhimg_url"])
        return img_list

    def save_img_list(self, img_list):
        for img in img_list:
            self.save_img(img)

    @retry(stop_max_attempt_number=3)  #当保存图片出现异常的时候  就需要用retry   进行回滚  , 再次 保存当前图片 stop_max_attempt_number   重试的次数的次数
    def save_img(self, img):  # j对获取的 图片url进行下载 保存到本地
        f = open("G:\\Flask\\static/img1/" + str(self.num) + ".jpg", "wb")
        f.write((urllib.request.urlopen(img)).read())
        # time.sleep(10)
        print(str(self.num) + "保存成功")
        self.num += 1

    def run(self):  # 实现主要逻辑
        total = 1500
        while self.num <= total:
            # 1获取链接
            url = self.temp_url.format(self.num)
            # 获取数据
            img_list = self.get_img_list(url)
            # 保存数据
            self.save_img_list(img_list)
            # 不要获取数据过于频繁
            # time.sleep(60)
            print("先休息一会")


if __name__ == '__main__':
    img = Img('赵丽颖')
    img.run()

