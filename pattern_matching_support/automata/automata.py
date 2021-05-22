from pattern_matching_support.automata.node import Node

class Automata:
    node: Node
    debug: bool

    def __init__(self, debug: bool = False, add: bool = True):
        self.node = Node("ε")
        self.debug = debug

    def add_transitions(self, node_name: str, transitions: list):
        k = 0
        current_node = self.node
        while k < len(transitions):
            is_new = False
            new_node = current_node.get_node_by_transition(transitions[k])
            is_final = k + 1 == len(transitions)
            if new_node is None:
                new_node = Node()
                new_node.is_final = is_final
                if is_final:
                    new_node.name = node_name
                is_new = True
            else:
                if is_final:
                    new_node.is_final = True

            final_str = ''
            if new_node.is_final:
                final_str = '*'
            if is_new and self.debug:
                print('(' + str(current_node.instance_index) + ', ' + str(current_node.name) + ')  --' +
                      transitions[k] + '--> (' + str(new_node.instance_index) + ', ' + str(new_node.name) + final_str + ')')
            current_node.add_transition(transitions[k], new_node)
            current_node = new_node
            k += 1

    def match(self, words: list):
        if len(words) == 0:
            return None
        k = 0
        current_node = self.node
        while True:
            word = None
            if k < len(words):
                word = words[k]
            node = None
            if word is not None:
                node = current_node.get_node_by_transition(word)
            if node is None:
                if current_node.is_final:
                    return current_node.name
                if k + 1 >= len(words):
                    return None
            else:
                if k + 1 >= len(words):
                    if not node.is_final:
                        return current_node.name
                current_node = node
            k += 1

