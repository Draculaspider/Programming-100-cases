"""
方言，又称”白话“”土话“或”土音“，指的是区别于标准得某一地区的语言。中国地域广阔，汉语与少数民族的方言众多。汉族社会
在发展过程中出现一批程度不同的分化和统一，因而使汉语逐渐产生了方言。东北方言，即东北官话，脱胎于冀鲁官话和胶辽官话,
是由当地各民族语言文化相互融合而产生的。本实例将实现东北方言的查询与浏览。输入一条东北方言,按下 Enter键即可查看其
解释,同时语音朗读东北方言及解释。如果输入的方言没有被査询到,则提示“没有检索到相关东北方言”。输入字母s,遍历全部东
北方言及其解释,并同步语音朗读。
"""

import winsound
import win32com
from win32com.client import Dispatch,constants
import random
import time

class ReadersOne:

    def __init__(self):
        self.speak_out = win32com.client.Dispatch('sapi.spvoice')
        self.lang={}

    def speak(self, str1):                                                # 按播放语音
        self.speak_out.speak(str1)                                        # 输出方言解释
        winsound.PlaySound(str1,winsound.SND_ASYNC)                       # 输出结束音

    def view(self):                                                       # 按字典顺序输出方言
        for key,value in self.lang.items():
            print(key,":",value)                                          # 按字典顺序显示方言
            self.speak(key+"     "+value)                                 # 按字典顺序语音播放方言
            time.sleep(1)                                                 # 循环间隔时间为1秒钟

    def read(self):
        with open("note.txt","r",encoding='UTF-8') as file:               # 读取文件中的方言给字典
            while True:
                line = file.readline()                                    # 按行读取内容
                if line =='':
                    break
                group=line.split("：")                                    # 按”：“分割字符串
                self.lang[group[0]]=group[1]

    def start(self):
        print("     东北方言\n")
        print("说明：输入”q“退出系统：输入”s“按顺序输出并朗读词典内容。")
        while True:
            word = input("请输入要查找的东北方言：").strip()                # 要求用户输入方言，对输入的方言去除空格等
            if word.lower() == "q":                                       # 输入q，退出系统
                break
            elif word.lower() == "s":                                     # 输入s,遍历方言
                self.read()
                self.view()
            else:
                self.read()
                note=self.lang.get(word,"no")                             # 查找输入的方言
                if note != "no":                                          # 查到，输出并朗读方言与解释
                    print(word,":",note)
                    self.speak(word+":     "+note)
                else:
                    print("没有检索到相关东北方言！")

re = ReadersOne()
re.start()
