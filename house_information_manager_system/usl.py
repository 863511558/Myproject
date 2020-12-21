"""
    用户显示层
"""
from bll import HouseManagerController


class HouseManagerView:
    def __init__(self):
        self.__controller = HouseManagerController()

    def __display_menu(self):
        print("按1键显示所有房源信息")
        print("按2键显示总价最高房源信息")
        print("按3键显示面积最小房源信息")
        print("按4键根据总价升序显示房源信息")
        print("按5键根据面积降序显示房源信息")
        print("按6键查找所有户型信息")

    def __select_menu(self):
        item = input("请输入选项：")
        if item == "1":
            self.__show_houses()
        elif item == "2":
            self.__max_money()
        elif item == "3":
            self.__min_acreage()
        elif item == "4":
            self.__up_ascending()
        elif item == "5":
            self.__down_acreage()
        elif item == "6":
            self.__door_information()
    def __show_houses(self):
        for house in self.__controller.list_houses:
            print(house)
    def __max_money(self):
        print(max(self.__controller.list_houses, key=lambda money: money.total_price))
    def __min_acreage(self):
        print(min(self.__controller.list_houses, key=lambda acreage: acreage.area))
    def __up_ascending(self):
       for item in  sorted(self.__controller.list_houses,key = lambda up:up.total_price):
           print(item)
    def __down_acreage(self):
        for item in sorted(self.__controller.list_houses, key=lambda down: down.area,reverse=True):
            print(item)
    def __door_information(self):
        dict_all_huxing={}
        for item in self.__controller.list_houses:
            if item.house_type in dict_all_huxing:
                dict_all_huxing[item.house_type]+=1
            else:
                dict_all_huxing[item.house_type]=1
        for k,v in dict_all_huxing.items():
            print(k,v)
    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()







