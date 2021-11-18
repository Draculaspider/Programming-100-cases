"""
编写一个商品竞猜价格游戏，用户可以选择竞猜商品，然后根据竞猜的商品竞猜价格，小于指定数字，提示“猜的价格小了...”；
用户输入大于指定数字，提示“猜的价格大了...”；如果输入的价格等于该商品的价格，则提示“恭喜，你猜对了！”
"""


class PriceCompetition:

    def __init__(self):
        self.list = [['小米手环4', 209], ['荣耀手环5', 199], ['华为手环B5', 849], ['ZNNCO智能血压手环', 379]]
        self.order = 0
        self.price = 0
        print("数字竞猜游戏！")
        print('可以竞猜的商品如下：\n', '1', self.list[0][0], '\n 2', self.list[1][0], '\n 3', self.list[2][0], '\n 4', self.list[3][0])

    def judge(self, guess):
        if guess.isdigit() == True:
            guess = int(guess)
            if guess == self.price:
                print("恭喜，你猜对了！")
            elif guess < self.price:
                print("猜的价格小了...")
            elif guess > self.price:
                print("猜的价格大了...")
            else:
                print("输入价格非法，请重新输入！")

    def start(self):
        number = input("请输入竞猜商品前面的数字：")         # 竞猜价格
        if number.isdigit() ==True:
            self.order = int(number)
            if self.order<4 and self.order>0:
                print("您选择的竞猜商品是：",self.list[self.order-1][0])
                self.price=self.list[self.order-1][1]
        guess = -1
        while guess != self.price:
            guess = input("请输入竞猜价格（只能输入整数价格）：")
            self.judge(guess)

Pr = PriceCompetition()
Pr.start()
