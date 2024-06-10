class IconFamily:
    '''
    图标族类，用于存储树形结构的图标
    '''
    def __init__(self, middle_node_icon: str, leaf_node_icon: str):
        self.middle_node_icon = middle_node_icon
        self.leaf_node_icon = leaf_node_icon

class PokerFaceIconFamily(IconFamily):
    '''
    扑克脸图标族
    '''
    def __init__(self):
        super().__init__("♢", "♤")
        # super().__init__("★", "❤")
