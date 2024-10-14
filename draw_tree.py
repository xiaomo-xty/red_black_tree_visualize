import json

# 加载 JSON 数据
def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

# 将红黑树转化为 Vis.js 所需的节点和边格式
def prepare_data(node):
    nodes = []
    edges = []

    def traverse(node, parent_id=None):
        if node is not None:
            node_id = len(nodes) + 1
            # 使用 \n 来换行
            nodes.append({
                'id': node_id,
                'label': f"{node['key']}\n({node['val']})",  # 使用 \n 换行
                'color': 'red' if node['color'] == 'red' else 'black',
                'shape': 'ellipse',  # 设置节点形状为圆形
                'width': 100,  # 设置节点宽度
                'height': 60,  # 设置节点高度
                'font': {'size': 16, 'color': 'white'}  # 字体样式
            })
            if parent_id is not None:
                edges.append({'from': parent_id, 'to': node_id})
            traverse(node.get('left'), node_id)
            traverse(node.get('right'), node_id)

    traverse(node)
    return nodes, edges

# 生成 HTML 文件
def create_html(nodes, edges):
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Red-Black Tree Visualization</title>
        <script type="text/javascript" src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script>
        <style>
            body {{
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background-color: #f0f0f0;
            }}
            #mynetwork {{
                width: 100%;
                height: 100%;
                border: 1px solid lightgray;
            }}
        </style>
    </head>
    <body>
        <div id="mynetwork"></div>
        <script type="text/javascript">
            var nodes = new vis.DataSet({json.dumps(nodes)});
            var edges = new vis.DataSet({json.dumps(edges)});
            var container = document.getElementById('mynetwork');
            var data = {{
                nodes: nodes,
                edges: edges
            }};
            var options = {{
                layout: {{
                    hierarchical: {{
                        direction: 'UD',  // 从上到下
                        sortMethod: 'directed'
                    }}
                }},
                physics: {{
                    enabled: true,  // 启用物理引擎
                    solver: 'repulsion',  // 使用排斥力算法，允许自由移动
                    repulsion: {{
                        centralGravity: 0.3,
                        springLength: 100,
                        springStrength: 0.1,
                        nodeDistance: 200  // 节点间距离
                    }},
                    stabilization: {{
                        iterations: 100,  // 稳定化迭代次数
                        updateInterval: 25
                    }}
                }},
                edges: {{
                    color: {{
                        color: 'lightgray',
                        highlight: 'orange'
                    }},
                    smooth: false
                }},
                interaction: {{
                    navigation: true,
                    dragView: true,  // 启用拖拽视图
                    selectable: true,  // 允许选择节点
                    dragNodes: true,  // 允许拖拽节点
                }}
            }};
            var network = new vis.Network(container, data, options);
        </script>
    </body>
    </html>
    """
    
    with open('red_black_tree_visualization.html', 'w') as f:
        f.write(html_content)

# 主程序
if __name__ == '__main__':
    json_file = 'tree.json'  # 因为文件在同一目录，所以直接使用文件名
    rb_tree = load_json(json_file)
    nodes, edges = prepare_data(rb_tree)
    create_html(nodes, edges)
    print("HTML 文件已生成，命名为 'red_black_tree_visualization.html'")
