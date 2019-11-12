orig_file = "all_tagged_sentences.txt"
amr_file = "amrs"

TAB_CHAR = "      "

def graphs_from_file(input_file):
    graphs, strings = [], []
    cur_gr_str = ""
    c = 0
    for line in open(input_file):
        if not line.split():
            if (cur_gr_str):
                graph = graph_from_string(cur_gr_str)
                graphs.append(graph)
                strings.append(cur_gr_str)
                s = string_from_graph(graph)
            cur_gr_str = ""
            c += 1
            if c > 5:
                break
            
        elif line[0] != "#":
            cur_gr_str += line
        
    return graphs, strings

def graph_from_string(parse_string):
    node_stack = []
    nodes = {}
    edges = []
    cur_node = None
    cur_edge = None

    
    for line in parse_string.split("\n"):
        if not line.strip():
            continue
        line_data = line.split()
        i = 0
        while i < len(line_data):
            item = line_data[i]
            if item[0] == "(":
                new_node = Node(item[1:], parent_ids = [], children_ids = [], attributes={})
                nodes[new_node.node_id] = new_node
                node_stack.append(new_node)
                
                if cur_node:
                    cur_node.children_ids.append(new_node.node_id)
                    new_node.parent_ids.append(cur_node.node_id)
                cur_node = new_node
            elif item == "/":
                cur_node.attributes["name"] = line_data[i+1].strip(")")
            elif item[0] == ":":
                if line_data[i+1][0] == "(":
                    cur_edge = Edge(cur_node.node_id, line_data[i+1][1:].strip(")"), item)
                    edges.append(cur_edge)
                elif line_data[i+1].strip(")") in nodes or ("~" in line_data[i+1] and line_data[i+1].split("~")[0] in nodes):
                    cur_edge = Edge(cur_node.node_id, line_data[i+1].strip(")"), item, new_node=False)
                    edges.append(cur_edge)                
                else:
                    cur_node.attributes[item] = line_data[i+1].strip(")")
            i += 1
            while (item.endswith(")")):
                item = item[:-1]
                node_stack.pop()
                if len(node_stack) > 0:
                    cur_node = node_stack[-1]
    return Graph(nodes, edges)

def string_from_graph(graph):
    res = []
    
    def print_node(node, parent, graph):
        edge = ""
        if parent:
            for i in range(len(graph.edges)):
                e = graph.edges[i]
                if e.parent_id == parent.node_id and e.child_id == node.node_id:
                    edge = graph.edges[i].value
                    
        res.append(str(edge + " (" + node.node_id + " / " + node.attributes["name"] + " " + " ".join([k + " " + v for k,v in node.attributes.items() if k != "name"])))
        if parent:
            for edge in [e for e in graph.edges if e.new_node == False and e.parent_id == node.node_id]:
                res.append(edge.value + " " + edge.child_id)
        
    def print_children(node, parent, graph):
        children = node.children_ids[:] # need a copy so we don't break the original
        print_node(node, parent, graph)
        while children:
            print_children(graph.node_dict[children.pop(0)], node, graph)
        res.append(")")
        
    def tab_out(res):
        tabs = 0
        i = 0
        
        while i < len(res):
            line = res[i]
            if line.strip() == ")":
                if res[i-1][-1] == " ":
                    res[i-1] = res[i-1].strip()
                res[i-1] += ")"
                res.pop(i)
            else:
                i += 1

        for i in range(len(res)):
            res[i] = TAB_CHAR*tabs + res[i] + (" " if not res[i].endswith(" ") else "")

            tabs += res[i].count("(")
            tabs -= res[i].count(")")

    print_children(graph.root, None, graph)
    tab_out(res)
    
    return "\n".join(res).strip()

class Graph(object):
    def __init__(self, nodes, edges):
        self.edges = edges
        self.node_dict = nodes
        self.root = None
        for node in nodes.values():
            if len(node.parent_ids) == 0:
                self.root = node
        
    def __str__(self):
        return "Nodes: " + str(self.node_dict) + "\nEdges: " + str(self.edges)

class Node(object):
    # head should be edge/node pairing, values are attributes on the node
    def __init__(self, node_id, parent_ids=[], attributes={}, children_ids=[]):
        self.node_id = node_id
        self.parent_ids = parent_ids
        self.attributes = attributes
        self.children_ids = children_ids

    def __repr__(self):
        return (str((self.node_id, self.parent_ids, self.children_ids, self.attributes)))
        

class Edge(object):
    def __init__(self, parent_id, child_id, value, new_node=True):
        self.parent_id = parent_id
        self.child_id = child_id
        self.value = value
        self.new_node = new_node
        
    def __repr__(self):
        return (str((self.parent_id, self.child_id, self.value)))

def tabs(line):
    return (len(line) - len(line.lstrip())) // 6

