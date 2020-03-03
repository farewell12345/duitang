from selenium import webdriver
import requests
import sys
import json
from browsermobproxy import Server
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import init_driver
def save_img(url,imagePath,name,i):

    r=requests.get(url)
    try:
        if(r.status_code==200):
            file=imagePath+name+'.png'
            f=open(file,'wb')
            f.write(r.content)
    except :
        print("遇到错误")
    finally:del r
def save_imagePath():
    print("请输入路径：")
    imagePath = input()
    try:
        out = open("index.txt", 'w+')
        out.write(imagePath + '\\')
        if out.readlines() != '':
            print("保存成功！")
        else:
            print("保存失败！")
    except:
        out = open("index.txt", 'a+')
        out.write(imagePath + '\\')
        if out.readlines() != '':
            print("保存成功！")
        else:
            print("保存失败！")
    return imagePath
def get_imagePath():
    try:
        with open('index.txt') as f:
            imagePath = f.read().rstrip()
    except:
        imagePath=save_imagePath()
    return imagePath
imagePath=get_imagePath()
i=0

src=input("请输入搜索关键字：如需更改下载路径请输入‘-1’ ")
if(src=="-1"):
    imagePath=save_imagePath()
    print("当前路径"+imagePath)
    src = input("请输入搜索关键字")
a=24
b=67
try:
    print("正在下载中……请稍后")
    while(a<120):

        url="https://www.duitang.com/napi/blog/list/by_search/?kw="+src+"&type=feed"
        uri=url+"&include_fields=top_comments%2Cis_root%2Csource_link%2Citem%2Cbuyable%2Croot_id%2Cstatus%2Clike_count%2Clike_id%2Csender%2Calbum%2Creply_count%2Cfavorite_blog_id&_type=&start="+str(a)+"&_=15832154044"+str(b)
        a=a+24
        response=requests.get(uri)
        #print(response.json())
        jsons=response.text
        json_obj =json.loads(jsons)
        result=json_obj['data']
        object_list=result['object_list']
        for obj in object_list:
            img=obj['photo']['path']
            name=str(obj['album']['name'])+str(obj['album']['id'])+str(obj['id'])+str(obj['sender']['id'])
            save_img(img,imagePath,str(name),str(i))
            i=i+1
    print("下载完成,图片保存于"+imagePath)
except :
    print("你的输入可能有错或网络出现问题！")

