"""
财务人员再计算工资或奖金时，有时需要手工对工作量、工作时间或者金额进行累加计算，很容易出现失误或计算错误，如果用程序计算，将变得简单
高效。本实例的数字累加器，可以帮助财务人员对需要的数字进行累加计算，即输入数字进行累加计算，按下Enter或者Q键退出程序
"""


class NumberAccumulator:

    def __init__(self):
        self.all = 0.0
        self.alladd = 0.0
        self.indig = ''

    def add(self, addin, data):                                             # 定义累加函数
        addone = addin + data
        return addone

    def is_number(self, s):                                                 # 定义判断数字函数
        try:
            float(s)
            return True
        except ValueError:
            pass

        try:
            import unicodedata

            unicodedata.numeric(s)
            return True
        except(TypeError, ValueError):
            pass

        return False

    def start(self):
        while True:
            self.indig = input("输入：").strip('')
            if self.indig == 'q' or self.indig == 'Q':
                break
            elif self.is_number(self.indig) == True:
                self.alladd = self.add(float(self.all), float(self.indig))  # 调用数字累加器
                self.all = format(self.alladd, '.2f')
                print(self.all)
            else:
                print("输入非法数字，请重新输入")


nu = NumberAccumulator()
nu.start()
