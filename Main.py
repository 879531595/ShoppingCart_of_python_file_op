#!/usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author: __Evin__
@file :  test.py
@time :  2017/08/{03}
@email:  879531595@qq.com
"""

'''
购物车
    用户入口，
    1、商品信息存在文件里
    2、已购商品，余额记录（第一次输入工资，之后不用）
    商家入口
    2、可以添加商品，修改商品价格
    3、
'''

userDatas = {
}

goods_prices = [
    # ('棒棒糖',0.5),
]

shoppingCart = []
'''
用户信息存储文件格式：
user：pass：power：wage\n
商品信息存储文件格式：
goods：price\n
'''

class FileOperate(object):
    def __init__(self):
        pass
    def user_data_read(self):
        with open('userList','r') as f:
            dataItem = f.readlines()
        for line in dataItem:
            item = line.strip()
            item = line.split(":")
            userDatas[item[0]] = dict()
            userDatas[item[0]]['username'] = item[0]
            userDatas[item[0]]['password'] = item[1]
            userDatas[item[0]]['power'] = item[2]
            userDatas[item[0]]['wage'] = int(item[3])

    def user_data_write(self):

        insertdata = []
        for item in userDatas:
            info = ''
            info += str(userDatas[item]['username'])
            info += ':'
            info += str(userDatas[item]['password'])
            info += ':'
            info += str(userDatas[item]['power'])
            info += ':'
            info += str(userDatas[item]['wage'])
            info += '\n'
            insertdata.append(info)

        with open('userList','w') as f:
            f.writelines(insertdata)

    def goods_data_read(self):
        with open('goods_price','r')as f:
            dataItem = f.readlines()
        for item in dataItem:
            item = item.strip()
            goods_prices.append(item.split(':'))

    def goods_data_write(self):
        insertList = []
        for item in goods_prices:
            info = ''
            info += item[0]
            info += ':'
            info += item[1]
            info += '\n'
            insertList.append(info)
        with open('goods_price','w') as f:
            for line in insertList:
                f.write(line)

class Main():
    f = FileOperate()

    def __init__(self):
        self.f.goods_data_read()
        self.f.user_data_read()
        self.userLogin_and_Decide()
        if self.power == '0':
            print('当前用户：普通用户')
            self.userMean()
        elif self.power == '1':
            print('当前用户：商家用户')
            self.merchantsMean()


    def userLogin_and_Decide(self):
        while True:
            username = input('please input your username:')
            if username in userDatas.keys():
                password = input('please input your password:')
                if password == userDatas[username]['password']:
                    print('Login success!')
                    self.username = username
                    self.power = userDatas[username]['power']
                    self.wage = userDatas[username]['wage']

                    break
                else:
                    print('password is error')
            else:
                print('your user is not eisxt')

    def userMean(self):
        if self.wage == 0:
            self.wage = input('please input your wage:')
            if self.wage.isdigit():
                self.wage = int(self.wage)
                userDatas[self.username]['wage'] = self.wage
            else:
                print('你输入的余额有误')
                exit()

        else:
            pass
        while True:
            for index , line in enumerate(goods_prices):
                print(index,'\t',line)
            choose = input('please input you want buy of index:')
            if choose.isdigit():
                choose = int(choose)
                n = len(goods_prices)

                if choose < n:
                    prices = int(goods_prices[choose][1])
                    if prices <= self.wage:
                        flag = input('你确定是要买吗（y/n）:')
                        if flag not in ['n','N']:
                            shoppingCart.append(goods_prices[choose])
                            self.wage -= prices
                            userDatas[self.username]['wage'] = self.wage
                            print('你的余额还剩【%s】' % self.wage)
                        else:
                            pass
                    else:
                        if prices > self.wage:
                            print('你的余额不够')
                else:

                    print('你的选项有问题')
            elif choose == 'b':
                print('你买了：')
                for info in shoppingCart:
                    print('\t\t【%s】' % info[0])
                print('你的余额是【%s】' % self.wage)
                self.f.user_data_write()
                break
            else:
                print('please well well input：')

    def merchantsMean(self):
        while True:
            print('''你的操作：\n1、添加商品\n2、删除商品\n3、修改商品\n4、显示商品''')

            choose = input('请输入你的选择：')
            if choose.isdigit():
                choose = int(choose)
                if choose == 1:
                    goods = input('请输入商品名称：')
                    prices = input('请输入商品价格：')
                    goods_prices.append([goods,prices])

                    print('添加成功')
                elif choose == 2:

                    goodsList = []
                    for i in goods_prices:
                        goodsList.append(i[0])
                    goods = input('请输入需要删除商品名称：')
                    if goods in goodsList:
                        index = goodsList.index(goods)
                        del goods_prices[index]
                        print('【%s】删除成功' % goods)
                    else:
                        print('你输入的商品名称不存在')

                elif choose == 3:
                    goodsList = []
                    for i in goods_prices:
                        goodsList.append(i[0])
                    goods = input('请输入需要修改商品名称：')
                    if goods in goodsList:
                        index = goodsList.index(goods)
                        goods_prices[index][1] = input('请输入修改后的价格')

                        print('【%s】修改成功' % goods)

                    else:
                        print('你输入的商品名称不存在')
                elif choose == 4:
                    print('当前商品：')
                    for index , line in goods_prices:
                        print(index,'\t',line)


            elif choose == 'b':
                self.f.goods_data_write()
                print('修改成功')



                break
            else:
                pass





if __name__ == "__main__":

    Main()



