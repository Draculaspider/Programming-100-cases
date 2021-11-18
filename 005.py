"""
产品序列号是在用户注册时根据用户软件所安装的计算机软硬件信息生成的唯一识别码，一般称作机器码，也叫序列号、认证码、
注册申请码等。本实例将介绍如何通过获取计算机上的硬盘序列号、CPU序列号、主板序列号，经过简单的加密过程，生成25位
的产品序列码。
该项目需要换值码和索引码，使用密码字典加密
"""
import wmi
import random
import os


class SerialNumber:

    def __init__(self):
        self.sec = "t95p0q_2.f6dz1cxmowgjensr7yh384bvualki"                             # 检索码
        self.dec = "dn7vhl.k_3wx1efsyc56zu2bomjtq8i0g4rp9a"                             # 换值码

    def Passworddict(self):                                                             # 随机生成检索码，换值码，本实例未调用该方法
        num = [chr(i) for i in range(97, 123)] + [chr(i) for i in range(48, 59)]
        random.shuffle(num)
        sec = ''.join(num)
        random.shuffle(num)
        dec = ''.join(num)

    def windowsinfo(self):
        c = wmi.WMI()
        for physical_disk in c.Win32_DiskDrive():
            hard_seral = physical_disk.SerialNumber                                     # 获取硬盘序列号
            print("硬盘序列号为：", hard_seral)
        if len(hard_seral) > 6:
            hard_seral = hard_seral[-6:]
        else:
            print("硬盘修信息获取错误！")
            os.exit(0)

        for cpu in c.Win32_Processor():
            cpu_seral = cpu.ProcessorID.strip()                                         # 获取CPU序列号
            print("CPU序列号为：", cpu_seral)
        if len(cpu_seral) > 4:
            cpu_seral = cpu_seral[-4:]
        else:
            print("CPU信息获取错误！")
            os.exit(0)

        for board_id in c.Win32_BaseBoard():                                            # 获取主板序列号
            board_id = board_id.SerialNumber
            print("主板序列号为：", board_id)
        if len(board_id) > 6:
            board_id = board_id[-5:]
        else:
            print("主板信息获取错误！")
            os.exit(0)
        self.seral = hard_seral + cpu_seral + board_id
        print("注册码使用的硬件信息为：", self.seral)

    def deal_with_seral(self):
        cha_seral = ""
        for i in range(0, 14, 2):
            cha_seral += self.seral[14 - i] + self.seral[i + 1]                        # 字符串尾和首递进连接生成新的字符串
        cha_seral = cha_seral + self.seral[7]                                          # 字符串的中间值放到新字符串最后
        list_seral = list(cha_seral)                                                   # 字符串转为列表
        list_seral.reverse()                                                           # 列表反转
        rand_seral = ""
        for i in range(10):                                                            # 将前10个字符串和其位置索引（16进制）连接
            j = random.randint(1, len(list_seral))
            rand_seral += hex(j)[2:] + list_seral[j - 1]                               # hex(j)[2:]，去掉16进制前的符号0x
            list_seral.remove(list_seral[j - 1])
        rand_seral = ''.join(list_seral) + rand_seral                                  # 形成25位的字符串
        return rand_seral

    def sequence_code(self, rand_seral):                                               # 生成注册码方法
        low_seral = ""
        rand_seral = rand_seral.lower()
        for item in rand_seral:
            j = self.sec.index(item)                                                   # 返回注册信息得每个字母得索引值
            low_seral += self.dec[j]                                                   # 根据索引拿出换码值并添加
        low_seral = low_seral.upper()                                                  # 将小写全部转化为大写
        last_seral = low_seral[0:5] + "-" + low_seral[5:10] + "-" + low_seral[10:15] + "-" + low_seral[15:20] + "-" + low_seral[20:25]
        print("生成的注册码为：\n", last_seral)

    def start(self):                                                                   # 开始方法
        self.windowsinfo()
        rand_seral = self.deal_with_seral()
        self.sequence_code(rand_seral)


Se = SerialNumber()
Se.start()
