import json
from graphviz import Digraph

class RBNode:
    def __init__(self, key, val, color, left=None, right=None):
        self.key = key
        self.val = val
        self.color = color  # Color: "red" or "black"
        self.left = left
        self.right = right

class RBTree:
    def __init__(self):
        self.root = None

def load_tree_from_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)

    def build_tree(node_data):
        if not node_data:
            return None
        
        return RBNode(
            key=node_data['key'],
            val=node_data['val'],
            color=node_data['color'],
            left=build_tree(node_data.get('left')),
            right=build_tree(node_data.get('right'))
        )

    tree = RBTree()
    tree.root = build_tree(data)
    return tree

def add_nodes(graph, node):
    if node is None:
        return
    
    # 设置颜色的透明度和字体颜色
    fillcolor = "#cc0000" if node.color == "red" else "#666666"  # 深红和深灰
    fontcolor = "white"  # 字体颜色为白色

    # 创建节点
    graph.node(str(node.key), f"{node.key}\n{node.val}", style="filled", fillcolor=fillcolor, fontcolor=fontcolor)
    
    if node.left:
        graph.edge(str(node.key), str(node.left.key))
        add_nodes(graph, node.left)
    if node.right:
        graph.edge(str(node.key), str(node.right.key))
        add_nodes(graph, node.right)

def visualize_tree(tree):
    dot = Digraph()
    dot.attr(size='10,10')  # 设置图像大小，调整为合适的值以提高质量
    add_nodes(dot, tree.root)
    dot.render('red_black_tree', format='pdf', cleanup=True)  # 移除 dpi 参数
    # dot.view()  # 打开生成的图片

if __name__ == "__main__":
    # 从 JSON 文件加载树
    tree = load_tree_from_json("tree.json")
    
    # 可视化红黑树
    visualize_tree(tree)
