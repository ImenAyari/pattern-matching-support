import re

class AbstractNode:
    pass


class Node(AbstractNode):
    index: int = 0
    instance_index: int
    name: str
    transitions: dict  # Map<Word, List<Node>>
    is_final: bool

    def __init__(self, name: str = None):
        self.name = name
        self.is_final = False
        self.transitions = dict()
        Node.index += 1
        self.instance_index = Node.index

    def get_node_by_transition(self, word: str):
        if not word:
            raise Exception("Word is not defined.")
        r = self.transitions.get(word)
        if r is not None:
            return r
        for k in self.transitions.keys():
            if k[0] == '/' and k[-1] == '/':
                if re.match(k[1:-1], word, re.MULTILINE) is not None:
                    # print(k[1:-1])
                    node = self.transitions.get(k)
                    # print(node).groups()
                    self.add_transition(word, node)
                    return node
        return None

    def add_transition(self, word: str, node: AbstractNode):
        if not word:
            raise Exception("Word is not defined.")
        if not node:
            raise Exception("Node is not defined")

        if not self.transitions.get(word) is None:
            return

        self.transitions[word] = node
