"""
实例描述：两千多年前希腊的天文学家希巴斯为标示在黄道上运行的位置，将黄道分成十二个区段，依次为白羊、金牛、双子、巨蟹、狮子、处女、
天秤、天蝎、射手、摩羯、水瓶、双鱼十二个星群。在地球运转到每个星群所占时段所出生的婴儿，也就对应了相应的星座。本实例可以根据用户输入的
公历日期，判断属于那个星座，并输出该星座的标志。
"""


class constellation:

    def __init__(self):
        self.sdate = [21, 20, 21, 21, 22, 22, 23, 24, 24, 24, 23, 22]
        self.conts = ['魔羯座', '水瓶座', '双鱼座', '白羊座', '金牛座', '双子座', '巨蟹座', '狮子座', '处女座', '天秤座', '天蝎座', '射手座', '魔羯座']
        self.signs = ['♑', '♒', '♓', '♈', '♉', '♊', '♋', '♌', '♍', '♎', '♏', '♐', '♑']

    def panduan(self, birth):
        cbir = birth.split('-')                         # 分割年、月、日到列表
        cmonth = str(cbir[1])                           # 提取月数据
        cdate = str(cbir[2])                            # 提取日数据
        if int(cdate) < self.sdate[int(cmonth) - 1]:    # 如果日数据早于对应月列表中对应的日期
            print(self.conts[int(cmonth) - 1])          # 直接输出星座列表对应月的星座
            print(self.signs[int(cmonth) - 1])          # 直接输出星座列表对应月的星座
        else:
            print(self.conts[int(cmonth)])              # 否则输出星座列表下一月对应的星座
            print(self.signs[int(cmonth)])              # 否则输出星座列表下一月对应的星座

    def start(self):
        brith = input('请输入你的出生年月日，格式为：2001-02-21或2001-2-21\n').strip(' ')
        self.panduan(brith)


con = constellation()
con.start()                                             # 调用启动方法
