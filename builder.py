from styleFactory import AbstractStyleFactory

class JSONBuilder:
    '''
    建造者模式，负责将JSON数据转换为节点树
    '''
    def __init__(self, factory: AbstractStyleFactory):
        self.factory = factory

    def build(self, data: dict):
        root = self.factory.create_node("root")
        # 递归创建节点
        self.build_recursive(root, data)
        # 设置首行和末行
        self.set_first_row(root)
        self.set_last_row(root)
        return root

    def build_recursive(self, parent_node, data, level=0, isLastBlock=False):
        data_len = len(data)
        # 需要带有编号的遍历
        for i, (key, value) in enumerate(data.items()):
            # 如果是最后一块，就设置isLastBlock属性
            if level == 0 and i == data_len - 1:
                isLastBlock = True

            # 如果值是字典，则递归创建子节点
            if isinstance(value, dict):
                node = self.factory.create_node(key)
                parent_node.add_child(node)
                self.build_recursive(node, value, level+1, isLastBlock)
            # 如果值是字符串，则创建叶子节点
            else:
                node = self.factory.create_node(key, str(value))
                parent_node.add_child(node)

            # 设置节点的isFirst和isLast属性
            if i == 0:
                node.isFirst = True
            if i == data_len - 1:
                node.isLast = True

            # 设置节点的level属性
            node.level = level
            # 设置节点的isLastBlock属性
            node.isLastBlock = isLastBlock

    def set_first_row(self, root_node):
        root_node.children[0].isFirstRow = True
    
    def set_last_row(self, root_node):
        if len(root_node.children) > 1:
            self.set_last_row(root_node.children[-1])
        elif len(root_node.children) == 1:
            self.set_last_row(root_node.children[0])
        else:
            root_node.isLastRow = True
