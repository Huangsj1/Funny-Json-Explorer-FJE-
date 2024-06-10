from iconFamily import IconFamily

TRIANGLE_LENGTH = 45

class Node:
    '''
    基础节点类
    '''
    def __init__(self, name: str, value: str = None):
        self.name = name
        self.value = value
        self.children = []
        self.isFirst = False
        self.isLast = False
        self.isFirstRow = False
        self.isLastRow = False
        self.isLastBlock = False
        self.level = 0

    def add_child(self, child):
        self.children.append(child)

    def display(self, icon_family=None):
        raise NotImplementedError("Subclass must implement abstract method")
    
    def display_without_root(self, icon_family=None):
        raise NotImplementedError("Subclass must implement abstract method")
    

class TreeNode(Node):
    '''
    树形节点类，用于构建树形结构
    '''
    def display(self, icon_family=None):
        # 防止展示root节点
        for child in self.children:
            child.display_without_root(icon_family=icon_family)

    def display_without_root(self, icon_family=None):
        # 如果有图标族就使用图标族的图标
        if icon_family is not None:
            if len(self.children) == 0:
                icon = icon_family.leaf_node_icon
            else:
                icon = icon_family.middle_node_icon
        else:
            icon = " "
        # icon += " "

        # 如果有value就对value进行处理
        if self.value is not None and self.value != "None":
            self.value = f": {self.value}"
        else:
            self.value = ""

        # 根据层级构建前缀
        prefix = ""
        if self.level > 0:
            if self.isLastBlock:
                prefix += "   " * (self.level - 1) + "   "
            else:
                prefix += "│  " + (self.level - 1) * "   "

        # 前缀的打印
        if self.isLast:
            print(prefix + "└─" + icon + self.name + self.value)
        else:   
            print(prefix + "├─" + icon + self.name + self.value)

        # 递归打印子节点
        for child in self.children:
            child.display_without_root(icon_family=icon_family)


class RectangleNode(Node):
    '''
    矩形节点类，用于构建矩形结构
    '''
    def display(self, icon_family=None):
        # 防止展示root节点
        for child in self.children:
            child.display_without_root(icon_family=icon_family)

    def display_without_root(self, icon_family=None):
        # 如果有图标族就使用图标族的图标
        if icon_family is not None:
            if len(self.children) == 0:
                icon = icon_family.leaf_node_icon
            else:
                icon = icon_family.middle_node_icon
        else:
            icon = " "
        # icon += " "

        # 如果有value就对value进行处理
        if self.value is not None and self.value != "None":
            self.value = f": {self.value}"
        else:
            self.value = ""

        if self.isFirstRow:
            cur_str = "┌─" + icon + self.name + self.value + " "
            print(cur_str + (TRIANGLE_LENGTH - len(cur_str) - 1) * "─"  + "┐")
        elif self.isLastRow:
            cur_str = "└──" * self.level +  "└─" + icon + self.name + self.value + " "
            print(cur_str + (TRIANGLE_LENGTH - len(cur_str) - 1) * "─"  + "┘")
        else:
            cur_str = "|  " * self.level + "├─" + icon + self.name + self.value + " "
            print(cur_str + (TRIANGLE_LENGTH - len(cur_str) - 1) * "─"  + "┤")

        # 递归打印子节点
        for child in self.children:
            child.display_without_root(icon_family=icon_family)