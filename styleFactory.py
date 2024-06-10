from abc import ABC, abstractmethod
from node import TreeNode, RectangleNode

class AbstractStyleFactory(ABC):
    '''
    抽象工厂类
    '''
    @abstractmethod
    def create_node(self, name: str, value: str = None):
        pass

class TreeStyleFactory(AbstractStyleFactory):
    '''
    树形风格工厂类，用于创建树形节点
    '''
    def create_node(self, name: str, value: str = None):
        return TreeNode(name, value)

class RectangleStyleFactory(AbstractStyleFactory):
    '''
    矩形风格工厂类，用于创建矩形节点
    '''
    def create_node(self, name: str, value: str = None):
        return RectangleNode(name, value)

class StyleFactory:
    '''
    提供使用的工厂类，用于根据风格类型创建对应的工厂
    '''
    @staticmethod
    def get_factory(style_type: str):
        if style_type == "tree":
            return TreeStyleFactory()
        elif style_type == "rectangle":
            return RectangleStyleFactory()
        else:
            raise ValueError(f"Unknown style type: {style_type}")
