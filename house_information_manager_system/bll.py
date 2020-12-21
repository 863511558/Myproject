"""
    业务逻辑层
""" 
from dal import HouseDao

class HouseManagerController:
    def __init__(self):
        self.__list_houses = HouseDao.load()

    @property
    def list_houses(self):
        """
            所有房源信息
        """
        return self.__list_houses
